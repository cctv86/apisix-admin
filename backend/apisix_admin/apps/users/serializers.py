from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=32, label="用户名")
    password = serializers.CharField(required=True, max_length=100, label="密码", write_only=True)
    is_superuser = serializers.BooleanField(label="是否管理员", default=False)

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "is_superuser")
