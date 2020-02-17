from django.urls import path, re_path, include
from .views import PluginsViewSet

app_name = "sni"


urlpatterns = [
   re_path(r'list/$', PluginsViewSet.as_view({"get": "list"})),
]