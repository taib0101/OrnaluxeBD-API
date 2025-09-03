from .base import Base
from src.models import dict_model, DictModel

class AdminRepo(Base):

    def __init__(self, model_dict: DictModel):
        super().__init__(model_dict=dict_model)


admin_repos = AdminRepo(model_dict=dict_model)