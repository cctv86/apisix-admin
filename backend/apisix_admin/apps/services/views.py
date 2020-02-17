from rest_framework import viewsets


class ServiceViewSet(viewsets.GenericViewSet):
    def __init__(self):
        self.url_suffix = "apisix/admin/services"
