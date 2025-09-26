from django.db import models

from src.utils import unique_id

class Role(models.Model):

    serial_number = models.IntegerField(unique=True, null=False)
    role_id = models.CharField(primary_key=True, default=unique_id, unique=True)
    role_name = models.CharField(max_length=100, unique=True, null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)
    
    class Meta:
        db_table = "roles"
        indexes = [
            models.Index(fields=["serial_number"]),
            models.Index(fields=["role_id"]),
            models.Index(fields=["role_name"])
        ]

    # override for autoincrement
    def save(self, *args, **kwargs):
        last = Role.objects.order_by("-serial_number").first()
        self.serial_number = (last.serial_number + 1) if last else 1
        super().save(*args, **kwargs)


class User(models.Model):

    serial_number = models.IntegerField(unique=True, null=False)
    user_id = models.CharField(primary_key=True, default=unique_id, unique=True)

    # One to One                   # on delete cascade                  # back_populates like sqlalchemy
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name="users")
    role_name = models.CharField(max_length=100, null=False)
    user_name = models.CharField(max_length=300, null=False)
    email = models.EmailField(max_length=300, unique=True, null=False)
    phone = models.CharField(max_length=11, unique=True, null=False)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "users"
        indexes = [
            models.Index(fields=["serial_number"]),
            models.Index(fields=["user_id"]),
            models.Index(fields=["user_name"]),
            models.Index(fields=["role_id"]),
            models.Index(fields=["role_name"]),
            models.Index(fields=["email"]),
            models.Index(fields=["phone"])
        ]

    def save(self, *args, **kwargs):
        last = User.objects.order_by("-serial_number").first()
        self.serial_number = (last.serial_number + 1) if last else 1
        super().save(*args, **kwargs)
    

class Category(models.Model):

    serial_number = models.IntegerField(unique=True, null=False)
    category_id = models.CharField(primary_key=True, default=unique_id, unique=True)
    category_name = models.CharField(max_length=300, null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "categories"
        indexes = [
            models.Index(fields=["serial_number"]),
            models.Index(fields=["category_id"]),
            models.Index(fields=["category_name"])
        ]

    def save(self, *args, **kwargs):
        last = Category.objects.order_by("-serial_number").first()
        self.serial_number = (last.serial_number + 1) if last else 1
        super().save(*args, **kwargs)


class Product(models.Model):

    serial_number = models.IntegerField(unique=True, null=False)
    product_id = models.CharField(primary_key=True, default=unique_id, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="categories")
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
        db_table = "products"
        indexes = [
            models.Index(fields=["serial_number"]),
            models.Index(fields=["product_id"]),
            models.Index(fields=["product_name"]),
            models.Index(fields=["category_id"]),
            models.Index(fields=["category_name"]),
            models.Index(fields=["unique_code"]),
            models.Index(fields=["total_price"]),
            models.Index(fields=["discount"]),
            models.Index(fields=["discount_price"]),
            models.Index(fields=["variant"])
        ]

    def save(self, *args, **kwargs):
        last = Product.objects.order_by("-serial_number").first()
        self.serial_number = (last.serial_number + 1) if last else 1
        super().save(*args, **kwargs)


class ProductImage(models.Model):

    serial_number = models.IntegerField(unique=True, null=False)
    product_image_id = models.CharField(primary_key=True, default=unique_id, unique=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="product_images")
    product_name = models.CharField(max_length=300, unique=False, null=False)
    image_string = models.CharField(max_length=300, unique=False, null=False)
    image_url = models.CharField(max_length=300, unique=False, null=False)
    bucket_string = models.CharField(max_length=300, unique=False, null=False)
    bucket_folder = models.CharField(max_length=300, unique=False, null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "product_images"
        indexes = [
            models.Index(fields=["serial_number"]),
            models.Index(fields=["product_image_id"]),
            models.Index(fields=["product_id"]),
            models.Index(fields=["product_name"]),
            models.Index(fields=["image_string"]),
            models.Index(fields=["image_url"]),
            models.Index(fields=["bucket_string"])
        ]

    def save(self, *args, **kwargs):
        last = ProductImage.objects.order_by("-serial_number").first()
        self.serial_number = (last.serial_number + 1) if last else 1
        super().save(*args, **kwargs)


class Rating(models.Model):

    serial_number = models.IntegerField(unique=True, null=False)
    rating_id = models.CharField(primary_key=True, default=unique_id, unique=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="ratings")
    product_name = models.CharField(max_length=300, unique=False, null=False)
    rating_number = models.IntegerField()
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "ratings"
        indexes = [
            models.Index(fields=["rating_id"]),
            models.Index(fields=["product_id"]),
            models.Index(fields=["rating_number"])
        ]
