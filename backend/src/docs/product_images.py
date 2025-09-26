from drf_spectacular.utils import extend_schema, OpenApiParameter

from src.schemas import ProductImageIn, ProductImageUpdate, ProductImageOut, ProductImageTotalOut, ProductImageDelete


def product_image_id_parameter(required: bool): 

    return OpenApiParameter(
        name="product_image_id",
        description="Enter your product image id",
        required=required,
        type=str
    )


def product_id_parameter(required: bool): 

    return OpenApiParameter(
        name="product_id",
        description="Enter your product id",
        required=required,
        type=str
    )


def create_product_image_base(request: ProductImageIn, responses: ProductImageOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Create A Single Base Product Image In a Table",
        description="Create A Single Base Product Image In a Table",
        tags=["Product Image"],
        request=request,
        responses=responses
    )


def read_product_image_all_base(request: None, responses: ProductImageTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read All Base Product Image In a Table",
        description="Read All Base Product Image In a Table",
        tags=["Product Image"],
        request=request,
        responses=responses
    )


def read_product_image_base(request: None, responses: ProductImageTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read A Single Base Product Image In a Table",
        description="Read A Single Base Product Image In a Table",
        tags=["Product Image"],
        parameters=[
            product_image_id_parameter(required=True)
        ],
        request=request,
        responses=responses
    )


def update_product_image_base(request: ProductImageUpdate, responses: ProductImageTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Update A Single Base Product Image In a Table",
        description="Update A Single Base Product Image In a Table",
        tags=["Product Image"],
        parameters=[
            product_image_id_parameter(required=True)
        ],
        request=request,
        responses=responses
    )


def delete_product_image_base(request: None, responses: ProductImageDelete):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Delete A Single Base Product Image In a Table",
        description="Delete A Single Base Product Image In a Table",
        tags=["Product Image"],
        parameters=[
            product_image_id_parameter(required=True)
        ],
        request=request,
        responses=responses
    )
