from django.urls import path

from src.views import RoleCreate, RoleRead, RoleReadAll, RoleUpdate, RoleDelete

roles_endpoint = [
    path("role/create", RoleCreate.as_view()),
    path("role/update", RoleUpdate.as_view()),
    path("role", RoleRead.as_view()),
    path("role/all", RoleReadAll.as_view()),
    path("role/delete", RoleDelete.as_view())
]