#coding: utf-8
from rest_framework import viewsets, permissions, status
from .models import Tenant, TenantGroup
from .serializers import TenantSerializer
from utils.base import BaseViewSet
from rest_framework.response import Response


class TenantViewSwt(viewsets.ModelViewSet):
    serializer_class = TenantSerializer
    queryset = Tenant.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tenant.objects.all().order_by("id")
        return Tenant.objects.filter(tenant__user__exact=self.request.user).order_by("id")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        qs = Tenant.objects.filter(url=request.data.get('url'))
        if len(qs) != 0:
            return Response({"ErrMsg": "base url is exist, please check."}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            serializer.save()
        else:
            tn = Tenant.objects.create(**serializer.validated_data)
            TenantGroup.objects.create(user=self.request.user, tenant_id=tn.id)


class TenantCheckViewSet(BaseViewSet):
    """
    健康检查接口
    """
    permission_classes = (permissions.IsAuthenticated,)

    def __init__(self):
        self.url_suffix = "apisix/status"

