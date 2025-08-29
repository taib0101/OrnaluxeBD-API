from django.urls import path

from src.views import RoleCreate, RoleRead, RoleReadAll, RoleUpdate, RoleDelete

users_endpoint = [
    # path("users/", UserViewSet.as_view(), name="users")
    path("roles/create", RoleCreate.as_view()),
    path("roles/update", RoleUpdate.as_view()),
    path("roles", RoleRead.as_view()),
    path("roles/all", RoleReadAll.as_view()),
    path("roles/delete", RoleDelete.as_view())
]