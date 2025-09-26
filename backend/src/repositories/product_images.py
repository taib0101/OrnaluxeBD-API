from .base import Base
from src.models import dict_model, DictModel
from src.supports import AppException, AppExceptionCase

class ProductImageRepo(Base):

    def __init__(self, model_dict: DictModel):
        super().__init__(model_dict=model_dict)


    def read_product_image_query(self, query_data: dict):
        data = self.read(ModelName="ProductImage", query_data=query_data)

        if isinstance(data, AppException):
            raise AppExceptionCase.NotFoundError("Not Found")
        
        return data

product_image_repos = ProductImageRepo(model_dict=dict_model)