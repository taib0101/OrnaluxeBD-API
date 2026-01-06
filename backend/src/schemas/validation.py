from rest_framework.exceptions import ValidationError

from src.supports import AppExceptionCase

def input_validation(SchemaName, data_in):
    data_in = SchemaName(data=data_in)
    data_in.is_valid(raise_exception=True)
    data_in = data_in.validated_data

    return data_in
    

def output_validation(SchemaName, data_out):
        data_out = SchemaName(instance=data_out) # or SchemaName(instance=data_out, many=True) it works like [{"data": "message"}]

        return data_out.data
    

