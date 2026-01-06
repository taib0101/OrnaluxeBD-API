from django.db import models


class BaseModel(models.Model):
    serial_number = models.IntegerField(unique=True, null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    # override for autoincrement
    def save(self, *args, **kwargs):
        last = self.__class__.objects.order_by("-serial_number").first()
        self.serial_number = (last.serial_number + 1) if last else 1
        super().save(*args, **kwargs)

    class Meta:
        abstract = True