#coding: utf-8
from utils.base import BaseViewSet


class SniViewSet(BaseViewSet):
    """
    SSL证书
    """
    def __init__(self):
        self.url_suffix = "apisix/admin/ssl"
