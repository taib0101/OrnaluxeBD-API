from django.urls import path, include
from src.endpoints import roles_endpoint

v1 = [
    path("v1/", include(roles_endpoint))
]