from django.urls import re_path
from .views import ServiceViewSet

app_name = "services"


urlpatterns = [
    re_path(r'list/', ServiceViewSet.as_view({"get": "list"})),
    re_path(r'', ServiceViewSet.as_view({"post": "create", "get": "list"})),
    re_path(r'(?P<pk>\d+)$', ServiceViewSet.as_view({'get': 'retrieve', 'put': 'update', "delete": "destroy"})),
]
