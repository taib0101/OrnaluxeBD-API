from rest_framework import serializers


class ProductRatingBase(serializers.Serializer):
    rating_number = serializers.IntegerField()

class ProductRatingIn(ProductRatingBase):
    product_id = serializers.CharField()

class ProductRatingUpdate(ProductRatingBase):
    pass

class ProductRatingOut(ProductRatingBase):
    rating_id = serializers.CharField()
    product_id = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField(required=False, allow_null=True)

class ProductRatingTotalOut(serializers.Serializer):
    total = serializers.IntegerField()
    data = ProductRatingOut(many=True)

class ProductRatingDelete(serializers.Serializer):
    message = serializers.CharField()
