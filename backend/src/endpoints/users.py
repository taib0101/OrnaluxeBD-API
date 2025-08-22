from django.urls import path, include

from src.views import UserViewSet

users_endpoint = [
    path("users/", UserViewSet.as_view(), name="users")
]