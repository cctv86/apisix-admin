from django.db import models
from django.conf import settings


class Tenant(models.Model):
    url = models.CharField(max_length=250, unique=True, verbose_name="url地址")
    location = models.CharField(max_length=250, verbose_name="位置")
    AUTH_CHOICES = (
        (u"NoAuth", "NoAuth"),
        (u"JWT", "JWT"),
        (u"KeyAuth", "KeyAuth"),
    )
    authType = models.CharField(max_length=10, choices=AUTH_CHOICES, default="NoAuth", verbose_name="认证类型")
    username = models.CharField(max_length=32, null=True, blank=True, verbose_name="用户名")
    password = models.CharField(max_length=100, null=True, blank=True, verbose_name="密码")
    token = models.CharField(max_length=100, null=True, blank=True, verbose_name="token")
    desc = models.CharField(max_length=250, null=True, blank=True, verbose_name="描述")

    class Meta:
        verbose_name = "tenant"
        verbose_name_plural = "tenant"
        app_label = "tenant"

    def __str__(self):
        return self.url


class TenantGroup(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    tenant = models.ForeignKey('Tenant', on_delete=models.CASCADE, related_name="tenant")

    class Meta:
        verbose_name = "tenant_group"
        verbose_name_plural = "tenant_group"

    def __str__(self):
        return self.tenant.url
