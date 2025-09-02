from django.urls import path

from src.views import UserCreate, UserRead, UserReadAll, UserUpdate, UserDelete

users_endpoint = [
    path("users/create", UserCreate.as_view()),
    path("users/update", UserUpdate.as_view()),
    path("users", UserRead.as_view()),
    path("users/all", UserReadAll.as_view()),
    path("users/delete", UserDelete.as_view())
]