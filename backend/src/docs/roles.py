from drf_spectacular.utils import extend_schema, OpenApiParameter, inline_serializer

from src.schemas import RoleIn, RoleOut, RoleTotalOut, RoleDelete

id_parameter = (
    OpenApiParameter(
        name="id",
        description="Enter your id",
        required=True,
        type=str
    )
)

def create_role(request: RoleIn, responses: RoleOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Create",
        description="Create a role",
        tags=["Role"],
        request=request,
        responses=responses
    )

def read_role_all(request: None, responses: RoleTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read",
        description="Read a role",
        tags=["Role"],
        request=request,
        responses=responses
    )

def read_role_query(request: None, responses: RoleTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read",
        description="Read a role",
        tags=["Role"],
        parameters=[id_parameter],
        request=request,
        responses=responses
    )

def update_role(request: RoleIn, responses: RoleTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Update",
        description="Update a role",
        tags=["Role"],
        parameters=[id_parameter],
        request=request,
        responses=responses
    )

def delete_role(request: None, responses: RoleDelete):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Delete",
        description="Delete a role",
        tags=["Role"],
        parameters=[id_parameter],
        request=request,
        responses=responses
    )