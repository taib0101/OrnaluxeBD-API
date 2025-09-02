from django.urls import path

from src.views import Login, Auth

auths_endpoint = [
    path("login", Login.as_view()),
    path("auth", Auth.as_view())
]