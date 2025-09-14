from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from src.schemas import UserIn, UserOut, UserTotalOut, UserUpdate, UserDelete

def id_parameter(required: bool): 

    return OpenApiParameter(
        name="user_id",
        description="Enter your id",
        required=required,
        type=str
    )


def mail_parameter(required: bool) : 

    return OpenApiParameter(
        name="email",
        description="Enter your mail",
        required=False,
        type=OpenApiTypes.EMAIL
    )


def mobile_number_parameter(required: bool):

    return OpenApiParameter(
        name="mobile_number",
        description="Enter your mobile number",
        required=False,
        type=str
    )


def create_user(request: UserIn, responses: UserOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Create A Single User",
        description="Create A Single User",
        tags=["User"],
        request=request,
        responses=responses
    )

def read_user_query(request: None, responses: UserTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read A Single User",
        description="Read A Single User",
        tags=["User"],
        parameters=[
            id_parameter(False), 
            mail_parameter(False), 
            mobile_number_parameter(False)
        ],
        request=request,
        responses=responses
    )

def read_user_all(request: None, responses: UserTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read All User",
        description="Read All User",
        tags=["User"],
        request=request,
        responses=responses
    )

def update_user(request: UserUpdate, responses: UserTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Update A Single User",
        description="Update A Single User",
        tags=["User"],
        parameters=[id_parameter(True)],
        request=request,
        responses=responses
    ) 

def delete_user(request: None, responses: UserDelete):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Delete A Single User",
        description="Delete A Single User",
        tags=["User"],
        parameters=[id_parameter(True)],
        request=request,
        responses=responses
    )