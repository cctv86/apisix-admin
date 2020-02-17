from rest_framework import viewsets
from utils.base import BaseViewSet


class ServiceViewSet(viewsets.GenericViewSet, BaseViewSet):
    def __init__(self):
        self.url_suffix = "apisix/admin/services"
