from django.db import models

from src.utils import unique_id

class Role(models.Model):

    serial_number = models.IntegerField(unique=True, null=False)
    role_id = models.CharField(primary_key=True, default=unique_id, unique=True)
    name = models.CharField(max_length=100, unique=True, null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)
    
    class Meta:
        db_table = "roles"
        models.Index(fields=["role_id"])

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
    name = models.CharField(max_length=300, null=False)
    email = models.EmailField(max_length=300, unique=True, null=False)
    phone = models.CharField(max_length=11, unique=True, null=False)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "users"
        models.Index(fields=["user_id"])
        models.Index(fields=["email"])
        models.Index(fields=["phone"])

    def save(self, *args, **kwargs):
        last = User.objects.order_by("-serial_number").first()
        self.serial_number = (last.serial_number + 1) if last else 1
        super().save(*args, **kwargs)
    