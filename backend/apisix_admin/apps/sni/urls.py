from django.urls import re_path
from .views import SniViewSet

app_name = "sni"


urlpatterns = [
   re_path(r'list/', SniViewSet.as_view({"get": "list"})),
   re_path(r'', SniViewSet.as_view({"post": "create", "get": "list"})),
   re_path(r'(?P<pk>\d+)$', SniViewSet.as_view({'get': 'retrieve', 'put': 'update', "delete": "destroy"})),
]