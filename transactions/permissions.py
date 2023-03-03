import ipdb

from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Account


class AccountDeactivated(permissions.BasePermission):
    def has_permission(self, request, view):
        account_id = view.kwargs.get("pk")
        account = Account.objects.get(id=account_id)
        ipdb.set_trace()
        if account.flag_ativo:
            return True
        raise PermissionDenied("You account must be active for this request.")
