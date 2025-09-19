from .base import Base
from src.models import dict_model, DictModel
from src.utils import Hash
from src.supports import AppException, AppExceptionCase

class AuthRepo(Base):

    def __init__(self, model_dict: DictModel):
        super().__init__(model_dict=model_dict)
        
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


auth_repos = AuthRepo(model_dict=dict_model)