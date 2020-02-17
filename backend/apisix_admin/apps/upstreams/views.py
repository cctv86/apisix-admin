#coding: utf-8
from rest_framework import viewsets
from utils.base import BaseViewSet


class UpstreamViewSet(viewsets.GenericViewSet, BaseViewSet):
    def __init__(self):
        self.url_suffix = "apisix/admin/upstreams"