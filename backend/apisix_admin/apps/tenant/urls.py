from django.urls import path, include, re_path
from .views import TenantViewSwt, TenantCheckViewSet
from rest_framework.routers import DefaultRouter

app_name = "tenant"
router = DefaultRouter()

router.register(r'group', TenantViewSwt)


urlpatterns = [
   re_path(r'status/$', TenantCheckViewSet.as_view({"get": "list"})),
   path(r'', include(router.urls)),

]