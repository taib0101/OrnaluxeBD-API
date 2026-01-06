from .models import *

class Models:
    Role = Role
    User = User
    Category = Category
    Product= Product
    ProductImage = ProductImage
    Rating = Rating


Model = {
    key: value 
    for key, value in Models.__dict__.items() 
    if not key.startswith("__") # it filters __module__ tuples
}
