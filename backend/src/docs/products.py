from drf_spectacular.utils import extend_schema, OpenApiParameter

from src.schemas import ProductIn, ProductUpdate, ProductOut, ProductTotalOut, ProductDelete

def product_id_parameter(required: bool): 

    return OpenApiParameter(
        name="product_id",
        description="Enter your product id",
        required=required,
        type=str
    )

def category_id_parameter(required: bool): 

    return OpenApiParameter(
        name="category_id",
        description="Enter your category id",
        required=required,
        type=str
    )

def create_product_base(request: ProductIn, responses: ProductOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Create A Single Base Product In a Table",
        description="Create A Single Base Product In a Table",
        tags=["Product"],
        request=request,
        responses=responses
    )


def read_product_all_base(request: None, responses: ProductTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read All Base Product In a Table",
        description="Read All Base Product In a Table",
        tags=["Product"],
        request=request,
        responses=responses
    )


def read_product_base(request: None, responses: ProductTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read A Single Base Product In a Table",
        description="Read A Single Base Product In a Table",
        tags=["Product"],
        parameters=[
            product_id_parameter(required=True)
        ],
        request=request,
        responses=responses
    )


def update_product_base(request: ProductUpdate, responses: ProductTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Update A Single Base Product In a Table",
        description="Update A Single Base Product In a Table",
        tags=["Product"],
        parameters=[
            product_id_parameter(required=True)
        ],
        request=request,
        responses=responses
    )


def delete_product_base(request: None, responses: ProductDelete):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Delete A Single Base Product In a Table",
        description="Delete A Single Base Product In a Table",
        tags=["Product"],
        parameters=[
            product_id_parameter(required=True)
        ],
        request=request,
        responses=responses
    )