from .base import *

from src.models import dict_model, DictModel

class CategoryRepo(Base):

    def __init__(self, model_dict: DictModel):
        super().__init__(model_dict=dict_model)

category_repos = CategoryRepo(model_dict=dict_model)