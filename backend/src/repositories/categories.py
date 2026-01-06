from .base import Base
from src.models import Model, Models
from src.supports import AppException, AppExceptionCase
class CategoryRepo(Base):

    def read_category_query(self, query_data: dict):
        data = self.read(ModelName="Category", query_data=query_data)

        if isinstance(data, AppException):
            raise data
        
        return data

category_repos = CategoryRepo()