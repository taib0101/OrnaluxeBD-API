from drf_spectacular.utils import extend_schema, OpenApiParameter

from src.schemas import ProductRatingIn, ProductRatingUpdate, ProductRatingOut, ProductRatingTotalOut, ProductRatingDelete


def product_rating_id_parameter(required: bool): 

    return OpenApiParameter(
        name="rating_id",
        description="Enter your product rating id",
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


def create_product_rating(request: ProductRatingIn, responses: ProductRatingOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Create A Single Base Product Rating In a Table",
        description="Create A Single Base Product Rating In a Table",
        tags=["Product Rating"],
        request=request,
        responses=responses
    )


def read_product_rating_all(request: None, responses: ProductRatingTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read All Base Product Rating In a Table",
        description="Read All Base Product Rating In a Table",
        tags=["Product Rating"],
        request=request,
        responses=responses
    )


def read_product_rating_query(request: None, responses: ProductRatingTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Read A Single Base Product Rating In a Table",
        description="Read A Single Base Product Rating In a Table",
        tags=["Product Rating"],
        parameters=[
            product_rating_id_parameter(required=True)
        ],
        request=request,
        responses=responses
    )


def update_product_rating(request: ProductRatingUpdate, responses: ProductRatingTotalOut):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Update A Single Base Product Rating In a Table",
        description="Update A Single Base Product Rating In a Table",
        tags=["Product Rating"],
        parameters=[
            product_rating_id_parameter(required=True)
        ],
        request=request,
        responses=responses
    )


def delete_product_rating(request: None, responses: ProductRatingDelete):

    return extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Delete A Single Base Product Rating In a Table",
        description="Delete A Single Base Product Rating In a Table",
        tags=["Product Rating"],
        parameters=[
            product_rating_id_parameter(required=True)
        ],
        request=request,
        responses=responses
    )
