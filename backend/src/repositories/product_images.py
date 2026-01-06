from .base import Base
from src.models import Model, Models
from src.supports import AppException, AppExceptionCase

class ProductImageRepo(Base):

    def read_product_image_query(self, query_data: dict):
        data = self.read(ModelName="ProductImage", query_data=query_data)

        if isinstance(data, AppException):
            raise data
        
        return data

product_image_repos = ProductImageRepo()