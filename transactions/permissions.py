import ipdb

from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Account
from rest_framework.exceptions import NotFound


class AccountDeactivated(permissions.BasePermission):
    def has_permission(self, request, view):
        account_id = view.kwargs.get("pk")
        try:
            account = Account.objects.get(id=account_id)
        except ObjectDoesNotExist:
            raise NotFound("Account not found")
        if account.flag_ativo:
            return True
        raise PermissionDenied("Your account must be active for this request.")
