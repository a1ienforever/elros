from rest_framework import permissions


class UpdateDeleteOrCreateRead(permissions.BasePermission):

    def has_permission(self, request, view):
        create_read = ("POST",) + permissions.SAFE_METHODS
        if request.method in create_read:
            return True
        else:
            return bool(request.user.is_authenticated)


