from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return User.objects.filter(pk=self.request.user).order_by("id")
        return User.objects.all().order_by("id")


