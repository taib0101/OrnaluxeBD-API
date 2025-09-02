from rest_framework.views import exception_handler
from rest_framework.response import Response


def handle_result(exception, context):
    response = exception_handler(exception, context)

    print("exception : ", exception)
    print("context: ", context)
    print("response: ", response)

    if response:
        return Response({"error": exception.message}, status=exception.status_code)

    return Response({"error": str(exception)}, status=500)