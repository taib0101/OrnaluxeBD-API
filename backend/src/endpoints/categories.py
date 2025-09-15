from django.urls import path

from src.views import CategoryCreate, CategoryRead, CategoryReadAll, CategoryUpdate, CategoryDelete

categories_endpoint = [
    path("category/create", CategoryCreate.as_view()),
    path("category/update", CategoryUpdate.as_view()),
    path("category", CategoryRead.as_view()),
    path("category/all", CategoryReadAll.as_view()),
    path("category/delete", CategoryDelete.as_view())
]