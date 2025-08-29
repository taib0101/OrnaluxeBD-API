from .models import *

class DictModel:
    Role = Role
    User = User


dict_model = {
    key: value 
    for key, value in DictModel.__dict__.items() 
    if not key.startswith("__") # it filters __module__ tuples
}
