from django.urls import path, include

from src.endpoints import (
    roles_endpoint, 
    users_endpoint, 
    auths_endpoint, 
    admins_endpoint, 
    categories_endpoint,
    products_endpoint
)

v1 = [
    path("v1/", include(roles_endpoint)),
    path("v1/", include(users_endpoint)),
    path("v1/", include(auths_endpoint)),
    path("v1/", include(admins_endpoint)),
    path("v1/", include(categories_endpoint)),
    path("v1/", include(products_endpoint))
]