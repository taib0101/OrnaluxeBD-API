from rest_framework.response import Response
from json import loads

from src.repositories import role_repos, RoleRepo
from src.schemas import RoleIn, RoleOut, RoleTotalOut, RoleUpdate, input_validation, output_validation

class RoleService:

    def __init__(self, repo: RoleRepo):
        self.repo = repo

    def create_role(self, request):
        requested_body = loads(request.body)

        data_in = input_validation(SchemaName=RoleIn, data_in=requested_body)

        data = self.repo.create(ModelName="Role", data_in=data_in, temp_write="no")
        data = output_validation(SchemaName=RoleOut, data_out=data)

        return Response(data, status=200)
    
    def read_role_all(self, request):
        data = self.repo.read_all(ModelName="Role")
        data = output_validation(SchemaName=RoleTotalOut, data_out=data)

        return Response(data, status=200)
    
    def read_role_query(self, request):
        query_data = request.GET.dict()

        data = self.repo.read_role_query(query_data=query_data)
        data = output_validation(SchemaName=RoleTotalOut, data_out=data)
    
        return Response(data, status=200)
    
    def update_role(self, request):
        requested_body = loads(request.body)
        
        data_update = input_validation(SchemaName=RoleUpdate, data_in=requested_body)

        query_data = request.GET.dict()

        data = self.repo.update(ModelName="Role", query_data=query_data, data_update=data_update, temp_write="no")
        data = output_validation(SchemaName=RoleTotalOut, data_out=data)

        return Response(data, status=200)
    
    def delete_role(self, request):
        query_data = request.GET.dict()

        data = self.repo.delete(ModelName="Role", query_data=query_data, temp_write="no")

        return Response(data, status=200)
    
role_services = RoleService(repo=role_repos)