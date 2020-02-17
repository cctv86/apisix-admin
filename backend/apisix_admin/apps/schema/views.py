# coding: utf-8
from django.http import JsonResponse
from rest_framework import viewsets
from utils.requests import request_session


class SchemaViewSet(viewsets.GenericViewSet):
    def __init__(self):
        self.url_suffix = "apisix/admin/schema/plugins"

    def list(self, request, *args, **kwargs):
        ret = request_session(request=request, action="list", url_suffix=self.url_suffix)
        if isinstance(ret, str):
            return JsonResponse({"Msg": ret})
        return JsonResponse({"Data": ret})
