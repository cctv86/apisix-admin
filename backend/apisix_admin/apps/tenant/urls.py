from django.urls import path, include
from .views import TenantGroupViewSet
from rest_framework.routers import DefaultRouter

app_name = "tenant"
router = DefaultRouter()

router.register(r'group', TenantGroupViewSet)


urlpatterns = [
   path(r'', include(router.urls)),
]