from drf_spectacular.utils import extend_schema


def sign_up(request, responses):

    return extend_schema(
        summary="SignUp Admin Initially",
        description="SignUp Admin Users",
        tags=["Admin"],
        request=request,
        responses=responses
    )