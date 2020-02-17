from django.urls import path, re_path, include
from .views import SchemaViewSet

app_name = "schema"


urlpatterns = [
   re_path(r'plugins/(?P<pk>\d+)$', SchemaViewSet.as_view({"get": "list"})),
]