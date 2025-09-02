from .base import Base
from src.models import dict_model, DictModel

class AuthRepo(Base):

    def __init__(self, model_dict: DictModel):
        super().__init__(model_dict)


auth_repos = AuthRepo(model_dict=dict_model)