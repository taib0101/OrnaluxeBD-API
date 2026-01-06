from django.db import models

from src.utils import unique_id
from .base import BaseModel


class Role(BaseModel):

    role_id = models.CharField(
        primary_key=True, default=unique_id, unique=True)
    role_name = models.CharField(max_length=100, unique=True, null=False)

    class Meta:
        abstract = False
        db_table = "roles"


class User(BaseModel):

    user_id = models.CharField(
        primary_key=True, default=unique_id, unique=True)

    # One to One                   # on delete cascade                  # back_populates like sqlalchemy
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, related_name="users")
    role_name = models.CharField(max_length=100, null=False)
    user_name = models.CharField(max_length=300, null=False)
    email = models.EmailField(max_length=300, unique=True, null=False)
    phone = models.CharField(max_length=11, unique=True, null=False)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = False
        db_table = "users"


class Category(BaseModel):

    category_id = models.CharField(
        primary_key=True, default=unique_id, unique=True)
    category_name = models.CharField(max_length=300, null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = False
        db_table = "categories"

class Product(BaseModel):

    product_id = models.CharField(
        primary_key=True, default=unique_id, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="categories")
    product_name = models.CharField(max_length=300, unique=False, null=False)
    category_name = models.CharField(max_length=300, unique=False, null=False)
    unique_code = models.CharField(max_length=100, unique=True, null=False)
    availability = models.BooleanField(default=True)
    total_price = models.FloatField()
    discount = models.FloatField()
    discount_price = models.FloatField()
    variant = models.JSONField(default=list, unique=False, null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = False
        db_table = "products"


class ProductImage(BaseModel):

    product_image_id = models.CharField(
        primary_key=True, default=unique_id, unique=True)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="product_images")
    product_name = models.CharField(max_length=300, unique=False, null=False)
    image_string = models.CharField(max_length=300, unique=False, null=False)
    image_url = models.CharField(max_length=300, unique=False, null=False)
    bucket_string = models.CharField(max_length=300, unique=False, null=False)
    bucket_folder = models.CharField(max_length=300, unique=False, null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = False
        db_table = "product_images"


class Rating(BaseModel):

    rating_id = models.CharField(
        primary_key=True, default=unique_id, unique=True)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="ratings")
    product_name = models.CharField(max_length=300, unique=False, null=False)
    rating_number = models.IntegerField(null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = False
        db_table = "ratings"