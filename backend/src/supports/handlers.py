from rest_framework.views import exception_handler
from rest_framework.response import Response


def handle_result(exception, context):
    print("exception : ", exception)
    print("context: ", context)

    response = exception_handler(exception, context)

    if response:
        return Response({"error": exception.message}, status=exception.status_code)

    return Response({"error": str(exception)}, status=500)