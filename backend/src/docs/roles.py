from drf_spectacular.utils import extend_schema, OpenApiParameter, inline_serializer

from src.schemas import RoleIn, RoleOut, RoleUpdate, RoleTotalOut, RoleDelete

id_parameter = (
    OpenApiParameter(
        name="role_id",
        description="Enter your id",
        required=True,
        type=str
    )
)

def create_role(request: RoleIn, responses: RoleOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Create A Single Role",
        description="Create A Single Role",
        tags=["Role"],
        request=request,
        responses=responses
    )

def read_role_all(request: None, responses: RoleTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read All Role",
        description="Read All Role",
        tags=["Role"],
        request=request,
        responses=responses
    )

def read_role_query(request: None, responses: RoleTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read A Single Role",
        description="Read a role",
        tags=["Role"],
        parameters=[id_parameter],
        request=request,
        responses=responses
    )

def update_role(request: RoleUpdate, responses: RoleTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Update A Single Role",
        description="Update A Single Role",
        tags=["Role"],
        parameters=[id_parameter],
        request=request,
        responses=responses
    )

def delete_role(request: None, responses: RoleDelete):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Delete A Single Role",
        description="Delete A Single Role",
        tags=["Role"],
        parameters=[id_parameter],
        request=request,
        responses=responses
    )