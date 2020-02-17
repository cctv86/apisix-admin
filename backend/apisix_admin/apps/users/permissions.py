from rest_framework import permissions


class ApiSixPermission(permissions.DjangoModelPermissions):

    def get_custom_perm(self, request):
        apisix_id = request.headers.get("apisix_id", None)
        apisix_url = request.headers.get("apisix_url", None)

        if apisix_id is None or apisix_url is None:
            return False
        try:
            return {"tenant_id": apisix_id} in list(request.user.user.values("tenant_id"))
        except Exception as e:
            return False

    def has_permission(self, request, view):
        if getattr(view, '_ignore_model_permissions', False):
            return True

        if request.user.is_superuser:
            return True

        if not request.user or (
                not request.user.is_authenticated and self.authenticated_users_only):
            return False

        return self.get_custom_perm(request)


# TODO: 组件权限控制, 例如services, ruotes, upstream ...