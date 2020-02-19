from django.http import JsonResponse
from utils.requests import request_session
from rest_framework import viewsets


class BaseViewSet(viewsets.GenericViewSet):
    def list(self, request, *args, **kwargs):
        ret = request_session(request=request, action="list", url_suffix=self.url_suffix)
        if isinstance(ret, str):
            return JsonResponse({"ErrMsg": ret})
        return JsonResponse(ret)

    def create(self, request, *args, **kwargs):
        ret = request_session(request=request, action="create", url_suffix=self.url_suffix, pk=kwargs.get("pk"))
        if isinstance(ret, str):
            return JsonResponse({"ErrMsg": ret})

        return JsonResponse(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = request_session(request=request, action="retrieve", url_suffix=self.url_suffix, pk=kwargs.get("pk"))
        if isinstance(ret, str):
            return JsonResponse({"ErrMsg": ret})
        return JsonResponse(ret)

    def update(self, request, *args, **kwargs):
        ret = request_session(request=request, action="update", url_suffix=self.url_suffix, pk=kwargs.get("pk"))
        if isinstance(ret, str):
            return JsonResponse({"ErrMsg": ret})
        return JsonResponse(ret)

    def destroy(self, request, *args, **kwargs):
        ret = request_session(request=request, action="destroy", url_suffix=self.url_suffix, pk=kwargs.get("pk"))
        if isinstance(ret, str):
            return JsonResponse({"ErrMsg": ret})
        return JsonResponse(ret)
