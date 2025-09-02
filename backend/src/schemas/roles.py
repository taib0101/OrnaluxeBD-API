from rest_framework import serializers

class RoleBase(serializers.Serializer):
    name = serializers.CharField()

class RoleIn(RoleBase):
    pass

class RoleOut(RoleBase):
    role_id = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField(required=False, allow_null=True)

class RoleTotalOut(serializers.Serializer):
    total = serializers.IntegerField()
    data = RoleOut(many=True)


class RoleUpdate(RoleIn):
    pass

class RoleDelete(serializers.Serializer):
    message = serializers.CharField()
