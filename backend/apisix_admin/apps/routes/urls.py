from django.urls import re_path
from .views import RouteViewSet

app_name = "routes"


urlpatterns = [
    re_path(r'list/', RouteViewSet.as_view({"get": "list"})),
    re_path(r'', RouteViewSet.as_view({"post": "create", "get": "list"})),
    re_path(r'(?P<pk>\d+)$', RouteViewSet.as_view({'get': 'retrieve', 'put': 'update', "delete": "destroy"})),
]
