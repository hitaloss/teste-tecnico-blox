from rest_framework import permissions


class AccountDeactivated(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.get_object().flag_ativo:
            return True
        return False
