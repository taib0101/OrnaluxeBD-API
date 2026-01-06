from .base import Base
from src.models import Model, Models
from src.supports import AppException, AppExceptionCase


class ProductRatingRepo(Base):

    def read_product_rating_query(self, query_data: dict):
        data = self.read(ModelName="Rating", query_data=query_data)

        if isinstance(data, AppException):
            raise data
        
        return data

product_rating_repos = ProductRatingRepo()
