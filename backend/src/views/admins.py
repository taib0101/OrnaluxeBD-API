from rest_framework.views import APIView

from src.docs import sign_up
from src.schemas import AdminIn
from src.services import admin_services

class AdminSignUp(APIView):

    authentication_classes = []

    @sign_up(request=AdminIn, responses=None)
    def post(self, request):
        if request.method == "POST":
            data = admin_services.create_inital_admin(request=request)

        return data
