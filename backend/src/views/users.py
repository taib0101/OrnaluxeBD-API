from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

# Define schema using a serializer
class GreetingSerializer(serializers.Serializer):
    message = serializers.CharField()

class UserViewSet(APIView):
    authentication_classes = []  

    @extend_schema(
        auth=[{"jwtAuth": []}],
        summary="Bro",
        description="Simple greeting endpoint",
        tags=["Shitt"],
        responses=GreetingSerializer
    )
    def get(self, request) -> Response:
        print("Request Authorization : ", request.headers['Authorization'])
        context = {
            "name": "Murtaza"
        }
        return Response(f"Hello, {context['name']}")