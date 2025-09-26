from .base import Base
from src.models import dict_model, DictModel
from src.supports import AppException, AppExceptionCase
class UserRepo(Base):

    def __init__(self, model_dict: DictModel):
        super().__init__(model_dict=model_dict)

    def read_user_query(self, query_data: dict):
        data = self.read(ModelName="User", query_data=query_data)

        if isinstance(data, AppException):
            raise AppExceptionCase.NotFoundError("Not Found")
        
        return data



user_repos = UserRepo(model_dict=dict_model)