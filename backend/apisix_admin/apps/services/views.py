#coding: utf-8
from utils.base import BaseViewSet


class ServiceViewSet(BaseViewSet):
    """
    Service
    """
    def __init__(self):
        self.url_suffix = "apisix/admin/services"
