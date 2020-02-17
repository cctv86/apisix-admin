from django.http import JsonResponse
from utils.requests import request_session


class BaseViewSet(object):
    def list(self, request, *args, **kwargs):
        ret = request_session(request=request, action="list", url_suffix=self.url_suffix)
        if isinstance(ret, str):
            return JsonResponse({"Msg": ret})
        if not ret.get('node').get('nodes', ''):
            return JsonResponse({"Msg": []})
        rst = {"Msg": "ok"}
        for item in ret.get('node').get('nodes'):
            rst[item["key"]] = item["value"]

        return JsonResponse(rst)

    def create(self, request, *args, **kwargs):
        ret = request_session(request=request, action="create", url_suffix=self.url_suffix, pk=kwargs.get("pk"))
        if isinstance(ret, str):
            return JsonResponse({"Msg": ret})
        if ret.get('errorCode', 0) != 0:
            return JsonResponse({"Msg": ret.get('message')})
        return JsonResponse({"Msg": "Success."})

    def retrieve(self, request, *args, **kwargs):
        ret = request_session(request=request, action="retrieve", url_suffix=self.url_suffix, pk=kwargs.get("pk"))
        if isinstance(ret, str):
            return JsonResponse({"Msg": ret})
        if ret.get('errorCode', 0) != 0:
            return JsonResponse({"Msg": ret.get('message')})

        value = ret.get("node").get("value")
        key = ret.get("node").get("key")
        rst = {
            "Msg": "ok",
            key: value
        }
        return JsonResponse(rst)

    def update(self, request, *args, **kwargs):
        ret = request_session(request=request, action="update", url_suffix=self.url_suffix, pk=kwargs.get("pk"))
        if isinstance(ret, str):
            return JsonResponse({"Msg": ret})
        if ret.get('errorCode', 0) != 0:
            return JsonResponse({"Msg": ret.get('message')})
        return JsonResponse({"Msg": "Success."})

    def destroy(self, request, *args, **kwargs):
        ret = request_session(request=request, action="destroy", url_suffix=self.url_suffix, pk=kwargs.get("pk"))
        if isinstance(ret, str):
            return JsonResponse({"Msg": ret})
        if ret.get('errorCode', 0) != 0:
            return JsonResponse({"Msg": ret.get('message')})
        return JsonResponse({"Msg": "Delete Success."})
