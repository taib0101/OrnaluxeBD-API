from rest_framework import serializers

class ProductImageBase(serializers.Serializer):
    product_name = serializers.CharField()
    image_string = serializers.CharField()
    image_url = serializers.CharField()
    bucket_string = serializers.CharField()
    bucket_folder = serializers.CharField()


class ProductImageIn(ProductImageBase):
    product_id = serializers.CharField()


class ProductImageUpdate(serializers.Serializer):
    product_name = serializers.CharField(required=False, allow_null=True)
    image_string = serializers.CharField(required=False, allow_null=True)
    image_url = serializers.CharField(required=False, allow_null=True)
    bucket_string = serializers.CharField(required=False, allow_null=True)
    bucket_folder = serializers.CharField(required=False, allow_null=True)


class ProductImageOut(ProductImageBase):
    product_id = serializers.CharField()
    product_image_id = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField(required=False, allow_null=True)


class ProductImageTotalOut(serializers.Serializer):
    total = serializers.IntegerField()
    data = ProductImageOut(many=True)


class ProductImageDelete(serializers.Serializer):
    message = serializers.CharField()

