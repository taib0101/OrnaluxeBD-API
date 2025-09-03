from rest_framework import serializers

class AdminIn(serializers.Serializer):
    role_name = serializers.CharField()
    user_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    password = serializers.CharField()
