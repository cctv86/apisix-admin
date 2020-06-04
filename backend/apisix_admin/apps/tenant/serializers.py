from rest_framework import serializers
from .models import Tenant
import re


class TenantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.CharField(required=True, max_length=250, label="url地址")
    location = serializers.CharField(required=True, max_length=250, label="位置")
    apiKey = serializers.CharField(write_only=True, max_length=200, label="api key")
    desc = serializers.CharField(max_length=250, label="描述", required=False)

    class Meta:
        model = Tenant
        fields = ("id", "url", "location", "apiKey", "desc")

    def validate_url(self, url):
        if not re.match("^http", url):
            raise serializers.ValidationError('url格式无效')
        return url
