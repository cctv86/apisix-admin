# coding: utf-8
import requests
import os
from tenant.models import Tenant
from django.conf import settings
from requests.exceptions import ConnectionError
import logging

methods = {
    "list": requests.get,
    "retrieve": requests.get,
    "destroy": requests.delete,
    "update": requests.put,
    "create": requests.post,
}


def get_tenant(url):
    try:
        tenant = Tenant.objects.get(url__exact=url)
    except Tenant.DoesNotExist:
        return "url target is not found."
    return tenant


def request_session(request, action, url_suffix, pk=None):
    func = methods.get(action)
    apisix_url = request.headers.get("api6Uri", "") or settings.APISIX_DEV_URL
    tenant = get_tenant(apisix_url)
    if isinstance(tenant, str):
        return tenant
    url = os.path.join(apisix_url, url_suffix)
    try:
        if pk is None:
            if tenant.authType == "NoAuth":
                if action == "create":
                    ret = func(url, json=request.data, timeout=(3, 10)).json()
                else:
                    ret = func(url, timeout=(3, 10)).json()
            elif tenant.authType == "KeyAuth":
                if action == "create":
                    ret = func(url, auth=(tenant.username, tenant.password), json=request.data, timeout=(3, 10)).json()
                else:
                    ret = func(url, auth=(tenant.username, tenant.password), timeout=(3, 10)).json()
            elif tenant.authType == "JWT":
                pass
            return ret
        else:
            if tenant.authType == "NoAuth":
                if action == "update":
                    ret = func(f"{url}/{pk}", json=request.data, timeout=(3, 10)).json()
                else:
                    ret = func(f"{url}/{pk}", timeout=(3, 10)).json()
            elif tenant.authType == "KeyAuth":
                if action == "update":
                    ret = func(f"{url}/{pk}", auth=(tenant.username, tenant.password), json=request.data, timeout=(3, 10)).json()
                else:
                    ret = func(f"{url}/{pk}", auth=(tenant.username, tenant.password), timeout=(3, 10)).json()
            elif tenant.authType == "JWT":
                pass
            return ret
    except ConnectionError as e:
        logging.error(e)
        return 'apisix connect errors'
