from django.urls import path, include, re_path
from .views import TenantGroupViewSet, TenantCheckViewSet
from rest_framework.routers import DefaultRouter

app_name = "tenant"
router = DefaultRouter()

router.register(r'group', TenantGroupViewSet)


urlpatterns = [
   re_path(r'status/$', TenantCheckViewSet.as_view({"get": "list"})),
   path(r'', include(router.urls)),

]