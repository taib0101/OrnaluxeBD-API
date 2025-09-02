from .base import Base
from src.models import dict_model, DictModel

class UserRepo(Base):

    def __init__(self, model_dict: DictModel):
        super().__init__(model_dict=dict_model)


user_repos = UserRepo(model_dict=dict_model)