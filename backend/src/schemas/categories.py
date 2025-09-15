from rest_framework import serializers

class CategoryBase(serializers.Serializer):
    name = serializers.CharField()

class CategoryIn(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    category_id = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField(required=False, allow_null=True)

class CategoryTotalOut(serializers.Serializer):
    total = serializers.IntegerField()
    data = CategoryOut(many=True)

class CategoryUpdate(CategoryBase):
    pass

class CategoryDelete(serializers.Serializer):
    message = serializers.CharField()
