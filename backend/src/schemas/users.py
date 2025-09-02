from rest_framework import serializers


class UserBase(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

class UserIn(UserBase):
    password = serializers.CharField()

class UserOut(UserBase):
    user_id = serializers.UUIDField()
    role_id = serializers.UUIDField(required=False, allow_null=True)
    role_name = serializers.CharField(required=False, allow_null=True)

class UserTotalOut(serializers.Serializer):
    total = serializers.IntegerField()
    data = UserOut(many=True)

class UserUpdate(UserBase):
    pass

class UserDelete(serializers.Serializer):
    message = serializers.CharField()