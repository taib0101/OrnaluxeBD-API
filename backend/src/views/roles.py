from rest_framework.response import Response
from rest_framework.views import APIView

from src.docs import create_role, read_role_query, read_role_all, update_role, delete_role

from src.schemas import RoleIn, RoleOut, RoleTotalOut, RoleUpdate, RoleDelete
from src.middleware import LoggedInAdmin
from src.services import role_services
from src.supports import AppExceptionCase

class RoleCreate(APIView):

    authentication_classes = [LoggedInAdmin]

    @create_role(request=RoleIn, responses=RoleOut)
    def post(self, request):
        if request.method == "POST":
            data = role_services.create_role(request=request)

        return data
    

class RoleRead(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_role_query(request=None, responses=RoleTotalOut)
    def get(self, request):
        if request.method == "GET":
            data = role_services.read_role_query(request=request)

        return data
    

class RoleReadAll(APIView):

    authentication_classes = [LoggedInAdmin]
    http_method_names = ['get']

    @read_role_all(request=None, responses=RoleTotalOut)
    def get(self, request):
        if request.method == "GET":
            data = role_services.read_role_all(request=request)

            return data

        raise AppExceptionCase.NotFoundError("NotFound")

class RoleUpdate(APIView):

    authentication_classes = [LoggedInAdmin]

    @update_role(request=RoleUpdate, responses=RoleTotalOut)
    def post(self, request):
        if request.method == "POST":
            data = role_services.update_role(request=request)

        return data
    
    
class RoleDelete(APIView):

    authentication_classes = [LoggedInAdmin]

    @delete_role(request=None, responses=RoleDelete)
    def get(self, request):
        if request.method == "GET":
            data = role_services.delete_role(request=request)

        return data
    
