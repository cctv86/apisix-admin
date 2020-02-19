#coding: utf-8
from utils.base import BaseViewSet


class ConsumerViewSet(BaseViewSet):
    """
    Consumer
    """
    def __init__(self):
        self.url_suffix = "apisix/admin/consumers"
