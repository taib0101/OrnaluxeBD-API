from django.urls import path

from src.views import ProductRatingCreate, ProductRatingAll, ProductRatingRead, ProductRatingUpdate, ProductRatingDelete

products_rating_endpoint = [
    path("product_rating/create", ProductRatingCreate.as_view()),
    path("product_rating/all", ProductRatingAll.as_view()),
    path("product_rating/", ProductRatingRead.as_view()),
    path("product_rating/update", ProductRatingUpdate.as_view()),
    path("product_rating/delete", ProductRatingDelete.as_view()),
]