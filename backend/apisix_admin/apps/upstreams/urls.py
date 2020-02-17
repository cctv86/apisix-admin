from django.urls import path, re_path
from .views import UpstreamViewSet

app_name = "upstreams"

urlpatterns = [
   re_path(r'list/', UpstreamViewSet.as_view({"get": "list"})),
   re_path(r'', UpstreamViewSet.as_view({"post": "create", "get": "list"})),
   re_path(r'(?P<pk>\d+)$', UpstreamViewSet.as_view({'get': 'retrieve', 'put': 'update', "delete": "destroy"})),
]