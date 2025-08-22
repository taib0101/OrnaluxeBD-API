from django.urls import path, include

from src.routers import v1


urlpatterns = [ 
    path("api/", include(v1))
]

