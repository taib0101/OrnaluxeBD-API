from .base import Base
from src.models import Model, Models
from src.utils import Hash
from src.supports import AppException, AppExceptionCase

class AuthRepo(Base):
        
    def login(self, query_data: dict):
        temp_data_in = query_data.copy()
        temp_data_in.pop('password')

        login_data = self.read(ModelName="User", query_data=temp_data_in)

        if isinstance(login_data, AppException):
            raise AppExceptionCase.UnAuthorized("Invalid Login")

        check_password = Hash.check_pass(query_data['password'], login_data['data'][0]['password'])

        if not check_password:
            raise AppExceptionCase.UnAuthorized("Invalid Login")
        
        return login_data


auth_repos = AuthRepo()