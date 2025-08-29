from rest_framework.views import APIView
from typing import List

from src.docs import create_role, read_role_query, read_role_all, update_role, delete_role
from src.schemas import RoleIn, RoleOut, RoleTotallOut, RoleUpdate, RoleDelete
from src.services import role_services


class RoleCreate(APIView):

    authentication_classes = []

    @create_role(request=RoleIn, responses=RoleOut)
    def post(self, request):
        if request.method == "POST":
            data = role_services.create_role(request=request)
        return data
    

class RoleRead(APIView):

    authentication_classes = []

    @read_role_query(request=None, responses=RoleTotallOut)
    def get(self, request):
        if request.method == "GET":
            data = role_services.read_role_query(request=request)
        return data
    
class RoleReadAll(APIView):

    authentication_classes = []

    @read_role_all(request=None, responses=RoleTotallOut)
    def get(self, request):
        if request.method == "GET":
            data = role_services.read_role_all(request=request)
        return data

class RoleUpdate(APIView):

    authentication_classes = []

    @update_role(request=RoleUpdate, responses=RoleTotallOut)
    def post(self, request):
        if request.method == "POST":
            data = role_services.update_role(request=request)

        return data
    

class RoleDelete(APIView):

    authentication_classes = []

    @delete_role(request=None, responses=RoleDelete)
    def get(self, request):
        if request.method == "GET":
            data = role_services.delete_role(request=request)

        return data
    
