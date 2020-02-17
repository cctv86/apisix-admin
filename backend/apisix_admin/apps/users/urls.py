from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserGroupViewSet


app_name = "users"
router = DefaultRouter()

router.register(r'user', UserGroupViewSet)


urlpatterns = [
   path(r'', include(router.urls)),
]