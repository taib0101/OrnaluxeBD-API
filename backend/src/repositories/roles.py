from .base import Base
from src.models import dict_model
from src.supports import AppException, AppExceptionCase

class RoleRepo(Base):

    def __init__(self, model_dict):
        super().__init__(model_dict)

    def read_role_query(self, query_data: dict):
        data = self.read(ModelName="Role", query_data=query_data)

        if isinstance(data, AppException):
            raise AppExceptionCase.NotFoundError("Not Found")
        
        return data



role_repos = RoleRepo(model_dict=dict_model)