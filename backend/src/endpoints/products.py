from django.urls import path

from src.views import ProductCreateBase, ProductReadAllBase, ProductReadBase, ProductUpdateBase, ProductDeleteBase

products_endpoint = [
    path("product/base/create", ProductCreateBase.as_view()),
    path("product/base/all", ProductReadAllBase.as_view()),
    path("product/base", ProductReadBase.as_view()),
    path("product/base/update", ProductUpdateBase.as_view()),
    path("product/base/delete", ProductDeleteBase.as_view()),
]