# coding: utf-8
import requests
import os
from tenant.models import Tenant
import logging

methods = {
    "list": requests.get,
    "retrieve": requests.get,
    "destroy": requests.delete,
    "update": requests.put,
    "create": requests.post,
}


def request_session(request, action, url_suffix, pk=None):
    func = methods.get(action)
    api6_uri = request.headers.get("API6URL")

    try:
        api6_apiKey = Tenant.objects.get(url=api6_uri).apiKey
    except Exception as e:
        logging.error(e)
        return "can not found api six instance"

    url = os.path.join(api6_uri, url_suffix)

    try:
        if pk is None:
            if action == "list" or action == "destroy":
                ret = func(url, timeout=5, headers={"X-API-KEY": api6_apiKey}).json()
                return ret
            else:
                ret = func(url, json=request.data, timeout=5, headers={"X-API-KEY": api6_apiKey}).json()
                return ret
        else:
            if action == "list" or action == "destroy":
                print(url, pk)
                ret = func(f"{url}/{pk}", timeout=5, headers={"X-API-KEY": api6_apiKey}).json()
                return ret
            else:
                ret = func(f"{url}/{pk}", json=request.data, timeout=5, headers={"X-API-KEY": api6_apiKey}).json()
                return ret
    except Exception as e:
        logging.error(e)
        return 'api6 connect errors'
