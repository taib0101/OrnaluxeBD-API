from django.urls import path

from src.views import ProductImageCreateBase, ProductImageReadAllBase, ProductImageReadBase, ProductImageUpdateBase, ProductImageDeleteBase

products_image_endpoints = [
    path("product_image/base/create", ProductImageCreateBase.as_view()),
    path("product_image/base/all", ProductImageReadAllBase.as_view()),
    path("product_image/base", ProductImageReadBase.as_view()),
    path("product_image/base/update", ProductImageUpdateBase.as_view()),
    path("product_image/base/delete", ProductImageDeleteBase.as_view()),
]