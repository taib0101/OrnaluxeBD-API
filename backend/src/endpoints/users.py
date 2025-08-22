from django.urls import path

from src.views import UserViewSet

users_endpoint = [
    path("users/", UserViewSet.as_view(), name="users")
]