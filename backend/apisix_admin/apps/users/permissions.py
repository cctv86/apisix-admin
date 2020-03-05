from rest_framework import permissions
import logging

class ApiSixPermission(permissions.DjangoModelPermissions):

    def get_custom_perm(self, request):
        apisix_id = request.headers.get("api6Id", None)
        apisix_url = request.headers.get("api6Uri", None)

        if apisix_id is None or apisix_url is None:
            return False
        try:
            return {"tenant_id": apisix_id} in list(request.user.user.values("tenant_id"))
        except Exception as e:
            logging.error(e)
            return False

    def has_permission(self, request, view):

        if not request.user or (
                not request.user.is_authenticated and self.authenticated_users_only):
            return False

        return self.get_custom_perm(request)


# TODO: 组件权限控制, 例如services, ruotes, upstream ...
