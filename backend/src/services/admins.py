from rest_framework.response import Response
from json import loads

from src.schemas import AdminIn, input_validation
from src.repositories import role_repos
from src.utils import Hash

class AdminService:

    def __init__(self, repo):
        self.repo = repo

    def create_inital_admin(self, request):
        requested_body = loads(request.body)

        admin_data = input_validation(SchemaName=AdminIn, data_in=requested_body)

        # role create of admin
        role_data = user_data = {}
        role_data['name'] = admin_data.pop('role_name')
        role_db_data = self.repo.create(ModelName="Role", data_in=role_data, temp_write="no")

        # user create of admin
        user_data['role_id'] = role_db_data['role_id']
        user_data['role_name'] = role_db_data['name']
        user_data['name'] = admin_data['user_name']
        user_data['email'] = admin_data['email']
        user_data['phone'] = admin_data['phone']
        user_data['password'] = Hash.create_pass(admin_data['password'])
        user_db_data = self.repo.create(ModelName="User", data_in=user_data, temp_write="no")

        return Response({'message': 'Created Successfully'}, status=200)
    

admin_services = AdminService(repo=role_repos)
