from django.urls import path, include
from src.endpoints import users_endpoint

v1 = [
    path("v1/", include(users_endpoint))
]