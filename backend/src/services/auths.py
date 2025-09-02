from rest_framework.response import Response
from json import loads

from src.repositories import auth_repos
from src.schemas import AuthLogIn, UserOut, input_validation, output_validation
from src.utils import Hash, Token
from src.supports import AppException, AppExceptionCase

class AuthService:

    def __init__(self, repo):
        self.repo = repo

    def login(self, request):
        requested_body = loads(request.body)

        data_in = input_validation(SchemaName=AuthLogIn, data_in=requested_body)

        if '@' in data_in['identifier'] and '.' in data_in['identifier']:
            data_in['email'] = data_in.pop('identifier')
        else:
            data_in['phone'] = data_in.pop('identifier')

        temp_data_in = data_in.copy()
        temp_data_in.pop('password')

        login_data = self.repo.read(ModelName="User", query_data=temp_data_in)

        check_password = Hash.check_pass(data_in['password'], login_data['data'][0]['password'])
        if isinstance(login_data, AppException) or not check_password:
            raise AppExceptionCase.UnAuthorized("Invalid Login")

        token = {
            'access_token': Token.create_token(
                login_data['data'][0]['user_id']
            ),
            'token_type': 'bearer'
        }

        return Response(token, status=200)

    def auth_check(self, request):
        token_credential = request.headers["Authorization"].split()[1]
        print("token_data : ", token_credential)

        token_to_data = Token.verify_token(token_credential)
        token_to_data['user_id'] = token_to_data.pop('sub')
        token_to_data.pop('exp')

        print("token_data : ", token_to_data)
        user_data = self.repo.read(ModelName="User", query_data=token_to_data)
        data = output_validation(SchemaName=UserOut, data_out=user_data['data'][0])

        return Response(data, status=200)

auth_services = AuthService(repo=auth_repos)