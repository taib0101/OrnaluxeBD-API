from .base import Base
from src.models import dict_model, DictModel
from src.supports import AppException, AppExceptionCase

class ProductRepo(Base):

    def __init__(self, model_dict: DictModel):
        super().__init__(model_dict=dict_model)

    def read_user_query(self, query_data: dict):
        data = self.read(ModelName="Product", query_data=query_data)

        if isinstance(data, AppException):
            raise AppExceptionCase.NotFoundError("Not Found")
        
        return data

product_repos = ProductRepo(model_dict=dict_model)