from rest_framework import serializers
from .models import Tenant, TenantGroup


class TenantSerializer(serializers.ModelSerializer):
    url = serializers.CharField(required=True, max_length=250, label="url地址")
    location = serializers.CharField(required=True, max_length=250, label="位置")
    authType = serializers.ChoiceField(choices=["JWT", "Session", "NoAuth"], label="认证类型")
    username = serializers.CharField(max_length=32, label="用户名", allow_blank=True, allow_null=True)
    password = serializers.CharField(max_length=32, label="密码", allow_blank=True, allow_null=True)
    token = serializers.CharField(max_length=32, label="token", allow_blank=True, allow_null=True)
    desc = serializers.CharField(max_length=250, label="描述")

    class Meta:
        model = Tenant
        fields = "__all__"


class TenantGroupSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer()

    class Meta:
        model = TenantGroup
        fields = ('tenant',)

