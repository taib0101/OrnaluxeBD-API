from .base import Base
from src.models import Model, Models
from src.supports import AppException, AppExceptionCase
class UserRepo(Base):

    def read_user_query(self, query_data: dict):
        data = self.read(ModelName="User", query_data=query_data)

        if isinstance(data, AppException):
            raise data
        
        return data


user_repos = UserRepo()