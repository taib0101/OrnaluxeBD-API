from rest_framework.response import Response
from json import loads

from src.repositories import user_repos
from src.schemas import UserIn, UserOut, UserTotalOut, UserUpdate, input_validation, output_validation
from src.utils import Hash

class UserService:

    def __init__(self, repo):
        self.repo = repo

    def create_user(self, request):
        requested_body = loads(request.body)

        data_in = input_validation(SchemaName=UserIn, data_in=requested_body)

        role_info = {
            'name': 'admin'
        }

        role_data = self.repo.read(ModelName="Role", query_data=role_info)

        data_in['role_id'] = role_data['data'][0]['role_id']
        data_in['role_name'] = role_data['data'][0]['name']
        data_in['password'] = Hash.create_pass(data_in['password'])

        user_data = self.repo.create(ModelName="User", data_in=data_in, temp_write="no")
        user_data['role_id'] = user_data.pop('role')
        user_data = output_validation(SchemaName=UserOut, data_out=user_data)

        return Response(user_data, status=200)
    
    def read_user_all(self, request):
        data = self.repo.read_all(ModelName="User")
        data = output_validation(SchemaName=UserTotalOut, data_out=data)

        return Response(data, status=200)
    
    def read_user_query(self, request):
        query_data = request.GET.dict()

        if 'mobile_number' in query_data:
            query_data['phone'] = query_data.pop('mobile_number')

        data = self.repo.read(ModelName="User", query_data=query_data)
        data = output_validation(SchemaName=UserTotalOut, data_out=data)

        return Response(data, status=200)

    def update_user(self, request):
        requested_body = loads(request.body)
        
        data_update = input_validation(SchemaName=UserUpdate, data_in=requested_body)

        query_data = request.GET.dict()

        data = self.repo.update(ModelName="User", query_data=query_data, data_update=data_update, temp_write="no")
        data = output_validation(SchemaName=UserTotalOut, data_out=data)

        return Response(data, status=200)
    
    def delete_user(self, request):
        query_data = request.GET.dict()

        data = self.repo.delete(ModelName="User", query_data=query_data, temp_write="no")

        return Response(data, status=200)



user_services = UserService(repo=user_repos)