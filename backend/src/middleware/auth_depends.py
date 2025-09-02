from rest_framework.authentication import BaseAuthentication

from src.services import auth_services
from src.supports import AppExceptionCase
from src.utils import Token

def logged_in(token_credential: str):
    token_to_data = Token.verify_token(token_credential)
    token_to_data['user_id'] = token_to_data.pop('sub')
    token_to_data.pop('exp')
    
    user_data = auth_services.repo.read(ModelName="User", query_data=token_to_data)

    return user_data['data'][0]['role_name']

def authorize_roles(token_credential: str, allowed_roles: list):
    role_name = logged_in(token_credential)
    if role_name not in allowed_roles:
        raise AppExceptionCase.UnAuthorized("UnAuthorized")


class LoggedInAdmin(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers["Authorization"]
        if not auth_header:
            raise AppExceptionCase.UnAuthorized("UnAuthorized")
        
        header_format = auth_header.split()
        if len(header_format) != 2 or header_format[0].lower() != 'bearer':
            raise AppExceptionCase.UnAuthorized("UnAuthorized")

        token_credential = header_format[1]

        authorize_roles(token_credential, allowed_roles=['admin'])