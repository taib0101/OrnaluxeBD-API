from .base import Base
from src.models import dict_model, DictModel
from src.supports import AppException, AppExceptionCase
class CategoryRepo(Base):

    def __init__(self, model_dict: DictModel):
        super().__init__(model_dict=dict_model)

    def read_category_query(self, query_data: dict):
        data = self.read(ModelName="Category", query_data=query_data)

        if isinstance(data, AppException):
            raise AppExceptionCase.NotFoundError("Not Found")
        
        return data

category_repos = CategoryRepo(model_dict=dict_model)