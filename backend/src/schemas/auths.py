from rest_framework import serializers


class AuthTokenOut(serializers.Serializer):
    access_token = serializers.CharField()
    token_type = serializers.CharField()


class AuthLogIn(serializers.Serializer):
    identifier = serializers.CharField()
    password = serializers.CharField()