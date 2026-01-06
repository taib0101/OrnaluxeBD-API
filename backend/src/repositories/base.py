from django.forms.models import model_to_dict
from django.db import transaction
from django.utils import timezone

from src.supports import AppExceptionCase
from src.models import Models, Model

class Base:

    Model: Models = Model

    def create(self, ModelName: str, data_in: dict, temp_write: str):
        with transaction.atomic():
            create_data = self.Model[ModelName].objects.create(**data_in, created_at=timezone.now())

            if temp_write == "yes":
                transaction.set_rollback(True)
                return None
            
        return model_to_dict(create_data)


    def read_all(self, ModelName: str):
        with transaction.atomic():
            read_data = self.Model[ModelName].objects.all()

        return {
            "total": len(read_data),
            "data": read_data
        }
    

    def read(self, ModelName: str, query_data: dict):
        with transaction.atomic():
            read_data = self.Model[ModelName].objects.filter(**query_data)

            if not read_data:
                return AppExceptionCase.NotFoundError("Not Found")

        return {
            "total": len(read_data),
            "data": list(read_data.values())
        }

        
    def update(self, ModelName: str, query_data: dict, data_update: dict, temp_write: str):
        with transaction.atomic():
            updated_data = self.Model[ModelName].objects.filter(**query_data).update(**data_update, updated_at=timezone.now())

            if not updated_data:
                raise AppExceptionCase.NotFoundError("Not Found")

            if temp_write == "yes":
                transaction.set_rollback(True)
                return None
        
            updated_data = self.read(ModelName, query_data)

        return updated_data
        
        

    def delete(self, ModelName: str, query_data: dict, temp_write: str):
        with transaction.atomic():
            delete_data = self.Model[ModelName].objects.filter(**query_data).delete()

            if not delete_data[0]:
                raise AppExceptionCase.NotFoundError("Not Found")

            if temp_write == "yes":
                transaction.set_rollback(True)
                return None

        return {
            "message": f"{delete_data[0]} data deleted"
        }