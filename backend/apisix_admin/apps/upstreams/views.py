# coding: utf-8
from utils.base import BaseViewSet


class UpstreamViewSet(BaseViewSet):
    """
    upstream
    """

    def __init__(self):
        self.url_suffix = "apisix/admin/upstreams"
