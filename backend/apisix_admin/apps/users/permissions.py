from rest_framework import permissions


class ApiSixPermission(permissions.DjangoModelPermissions):

    def get_custom_perm(self, request):

        api6_uri = request.headers.get("API6URL")
        if api6_uri is None or api6_uri == "undefined":
            return False
        return True

    def has_permission(self, request, view):

        if not request.user or (
                not request.user.is_authenticated and self.authenticated_users_only):
            return False

        return self.get_custom_perm(request)


# TODO: 组件权限控制, 例如services, ruotes, upstream ...