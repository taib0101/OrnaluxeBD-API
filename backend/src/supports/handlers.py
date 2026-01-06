from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.db import IntegrityError
from django.core.exceptions import FieldError

from .exceptions import AppExceptionCase, AppException

def custom_exception(exception, context):
    print("exception : ", exception)
    print("context: ", context)

    response = None

    if isinstance(exception, IntegrityError):
        response = exception_handler(AppExceptionCase.Conflict("Duplicate Value"), context)

    elif isinstance(exception, FieldError):
        response = exception_handler(AppExceptionCase.BadRequest("Bad Request for Database"), context)

    elif isinstance(exception, AppException):
        response = exception_handler(exception, context)

    print("response: ", response)

    return response


def handle_result(exception, context):

    response = custom_exception(exception=exception, context=context)

    if response:
        return Response({"error": response.data['detail']}, status=response.status_code)

    return Response({"error": str(exception)}, status=500)