from rest_framework import serializers
from .models import Tenant, TenantGroup


class TenantSerializer(serializers.ModelSerializer):
    url = serializers.CharField(required=True, max_length=250, label="url地址")
    location = serializers.CharField(required=True, max_length=250, label="位置")
    desc = serializers.CharField(max_length=250, label="描述")

    class Meta:
        model = Tenant
        fields = ('url', 'location', 'desc')


class TenantGroupSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer()

    class Meta:
        model = TenantGroup
        fields = ('tenant',)

