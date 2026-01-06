from .base import Base
from src.models import Model, Models
from src.supports import AppException, AppExceptionCase

class ProductRepo(Base):

    def read_product_query(self, query_data: dict):
        data = self.read(ModelName="Product", query_data=query_data)

        if isinstance(data, AppException):
            raise data
        
        return data

product_repos = ProductRepo()