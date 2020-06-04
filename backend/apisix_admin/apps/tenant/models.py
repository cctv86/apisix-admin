from django.db import models
from django.conf import settings


class Tenant(models.Model):
    url = models.CharField(max_length=250, unique=True, verbose_name="url地址")
    location = models.CharField(max_length=250, verbose_name="位置")
    apiKey = models.CharField(max_length=200, null=True, blank=True, verbose_name="apiKey")
    desc = models.CharField(max_length=250, null=True, blank=True, verbose_name="描述")

    class Meta:
        verbose_name = "tenant"
        verbose_name_plural = "tenant"
        app_label = "tenant"

    def __str__(self):
        return self.url


class TenantGroup(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="user")
    tenant = models.ForeignKey('Tenant', on_delete=models.CASCADE, related_name="tenant")

    class Meta:
        verbose_name = "tenant_group"
        verbose_name_plural = "tenant_group"

    def __str__(self):
        return self.tenant.url
