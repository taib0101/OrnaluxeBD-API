from django.urls import path

from src.views import AdminSignUp

admins_endpoint = [
    path("admin", AdminSignUp.as_view())
]