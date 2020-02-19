#coding: utf-8
from utils.base import BaseViewSet


class RouteViewSet(BaseViewSet):
    """
    Routes
    """
    def __init__(self):
        self.url_suffix = "apisix/admin/routes"

