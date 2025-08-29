from rest_framework.exceptions import APIException

class AppException(APIException):
    
    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class AppExceptionCase():
    
    class NotFoundError(AppException):
        def __init__(self, message):
            super().__init__(message, 404)

    class BadRequest(AppException):
        def __init__(self, message):
            super().__init__(message, 400)

    class DatabaseError(AppException):
        def __init__(self, message):
            super().__init__(message, 500)

