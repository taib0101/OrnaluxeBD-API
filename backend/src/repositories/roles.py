from .base import Base
from src.models import Model, Models
from src.supports import AppException, AppExceptionCase

class RoleRepo(Base):

    def read_role_query(self, query_data: dict):
        data = self.read(ModelName="Role", query_data=query_data)

        if isinstance(data, AppException):
            raise data
        
        return data


role_repos = RoleRepo()