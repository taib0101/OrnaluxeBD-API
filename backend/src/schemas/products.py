from rest_framework import serializers

class ProductVariant(serializers.Serializer):
    type = serializers.CharField(required=True, allow_blank=True)
    value = serializers.CharField(required=True, allow_blank=True)

class ProductBase(serializers.Serializer):
    product_name = serializers.CharField()
    category_name = serializers.CharField()
    unique_code = serializers.CharField()
    availability = serializers.BooleanField()
    total_price = serializers.FloatField()
    discount = serializers.FloatField()
    discount_price = serializers.FloatField()
    variant = serializers.ListField(child=ProductVariant())


class ProductIn(ProductBase):
    category_id = serializers.CharField()

class ProductUpdate(serializers.Serializer):
    product_name = serializers.CharField(required=False, allow_null=True)
    category_name = serializers.CharField(required=False, allow_null=True)
    unique_code = serializers.CharField(required=False, allow_null=True)
    availability = serializers.BooleanField(required=False, allow_null=True)
    total_price = serializers.FloatField(required=False, allow_null=True)
    discount = serializers.FloatField(required=False, allow_null=True)
    discount_price = serializers.FloatField(required=False, allow_null=True)
    variant = serializers.ListField(child=ProductVariant(), required=False, allow_null=True)

class ProductOut(ProductBase):
    product_id = serializers.CharField()
    category_id = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField(required=False, allow_null=True)

class ProductTotalOut(serializers.Serializer):
    total = serializers.IntegerField()
    data = ProductOut(many=True)

class ProductDelete(serializers.Serializer):
    message = serializers.CharField()


