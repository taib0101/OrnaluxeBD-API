from .base import Base
from src.models import Role
from src.models import dict_model

class RoleRepo(Base):

    def __init__(self, model_dict):
        super().__init__(model_dict)


role_repos = RoleRepo(model_dict=dict_model)