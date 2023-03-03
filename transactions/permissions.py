from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


# class AccountDeactivated(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if view.get_object().flag_ativo:
#             return True
#         raise PermissionDenied("You account must be active for this request.")
