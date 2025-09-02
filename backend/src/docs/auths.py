from drf_spectacular.utils import extend_schema, OpenApiParameter

from src.schemas import AuthLogIn, AuthTokenOut, UserOut

def login(request: AuthLogIn, responses: AuthTokenOut):

    return extend_schema(
        summary="Login",
        description="Login for authentication",
        tags=["Authentication"],
        request=request,
        responses=responses
    )

def auth_check(request: None, responses: UserOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Auth Check",
        description="Checking authentication",
        tags=["Authentication"],
        request=request,
        responses=responses
    )