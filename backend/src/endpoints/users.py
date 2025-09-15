from django.urls import path

from src.views import UserCreate, UserRead, UserReadAll, UserUpdate, UserDelete

users_endpoint = [
    path("user/create", UserCreate.as_view()),
    path("user/update", UserUpdate.as_view()),
    path("user", UserRead.as_view()),
    path("user/all", UserReadAll.as_view()),
    path("user/delete", UserDelete.as_view())
]