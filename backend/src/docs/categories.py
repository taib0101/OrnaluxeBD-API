from drf_spectacular.utils import extend_schema, OpenApiParameter

from src.schemas import CategoryIn, CategoryUpdate, CategoryOut, CategoryTotalOut, CategoryDelete

def id_parameter(): 

    return OpenApiParameter(
        name="category_id",
        description="Enter your id",
        required=True,
        type=str
    )

def create_category(request: CategoryIn, responses: CategoryOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Create A Single Category",
        description="Create A Single Category",
        tags=["Product Category"],
        request=request,
        responses=responses
    )

def read_category_query(request: None, responses: CategoryTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read A Single Category",
        description="Read A Single Category",
        tags=["Product Category"],
        parameters=[id_parameter()],
        request=request,
        responses=responses
    )


def read_category_all(request: None, responses: CategoryTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read All Category",
        description="Read All Category",
        tags=["Product Category"],
        request=request,
        responses=responses
    )

def update_category(request: CategoryUpdate, responses: CategoryTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Update A Single Category",
        description="Update A Single Category",
        tags=["Product Category"],
        parameters=[id_parameter()],
        request=request,
        responses=responses
    ) 

def delete_category(request: None, responses: CategoryDelete):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Delete A Single Category",
        description="Delete A Single Category",
        tags=["Product Category"],
        parameters=[id_parameter()],
        request=request,
        responses=responses
    )