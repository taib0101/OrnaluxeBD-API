from rest_framework.exceptions import ValidationError

from src.supports import AppExceptionCase, AppException

def input_validation(SchemaName, data_in):
    try:
        data_in = SchemaName(data=data_in)
        data_in.is_valid(raise_exception=True)
        data_in = data_in.validated_data

        return data_in

    except ValidationError:
        raise AppExceptionCase.BadRequest("Bad Request")
    

def output_validation(SchemaName, data_out):
    try:

        if not isinstance(data_out, AppException):
            data_out = SchemaName(instance=data_out) # or SchemaName(instance=data_out, many=True) it works like [{"data": "message"}]

            return data_out.data
    
        return data_out
    
    except ValidationError:
        raise AppExceptionCase.DatabaseError("Database Error")

