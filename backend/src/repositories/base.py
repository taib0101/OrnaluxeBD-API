from django.forms.models import model_to_dict
from django.db import transaction, IntegrityError
from django.utils import timezone

from src.supports import AppExceptionCase
from src.models import DictModel

def database_error_info(pg_error_code):
    print("pg code error : ", (pg_error_code))

    if pg_error_code == "23505":
        return AppExceptionCase.Conflict("Duplicate Value")
    elif pg_error_code == "23503":
        return AppExceptionCase.BadRequest("Bad Request for Foreign key violation")
    elif pg_error_code == "23502":
        return AppExceptionCase.BadRequest("Bad Request for Not Null violation")
    
    return AppExceptionCase.BadRequest("Bad Request for Database")

class Base:
    def __init__(self, model_dict: DictModel):
        self.model_dict = model_dict

    def create(self, ModelName: str, data_in: dict, temp_write: str):
        try:
            with transaction.atomic():
                create_data = self.model_dict[ModelName].objects.create(**data_in, created_at=timezone.now())

                if temp_write == "yes":
                    transaction.set_rollback(True)
                    return None
                
            return model_to_dict(create_data)
        
        except IntegrityError as integrity_exception:
            raise database_error_info(
                pg_error_code=integrity_exception.__cause__.pgcode
            )
    

    def read_all(self, ModelName: str):
        with transaction.atomic():
            read_data = self.model_dict[ModelName].objects.all()

        return {
            "total": len(read_data),
            "data": read_data
        }
    

    def read(self, ModelName: str, query_data: dict):
        with transaction.atomic():
            read_data = self.model_dict[ModelName].objects.filter(**query_data)

            if not read_data:
                return AppExceptionCase.NotFoundError("Not Found")

        return {
            "total": len(read_data),
            "data": list(read_data.values())
        }

        
    def update(self, ModelName: str, query_data: dict, data_update: dict, temp_write: str):
        try:
            with transaction.atomic():
                updated_data = self.model_dict[ModelName].objects.filter(**query_data).update(**data_update, updated_at=timezone.now())

                if not updated_data:
                    raise AppExceptionCase.NotFoundError("Not Found")

                if temp_write == "yes":
                    transaction.set_rollback(True)
                    return None
            
                updated_data = self.read(ModelName, query_data)

            return updated_data
        
        except IntegrityError as integrity_exception:
            raise database_error_info(
                pg_error_code=integrity_exception.__cause__.pgcode
            )
        

    def delete(self, ModelName: str, query_data: dict, temp_write: str):
        with transaction.atomic():
            delete_data = self.model_dict[ModelName].objects.filter(**query_data).delete()

            if not delete_data[0]:
                raise AppExceptionCase.NotFoundError("Not Found")

            if temp_write == "yes":
                transaction.set_rollback(True)
                return None

        return {
            "message": f"{delete_data[0]} data deleted"
        }
