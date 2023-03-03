from rest_framework import generics
from .models import Account
from .serializers import AccountsSerializer
from .serializers import AccountsBalanceDetailSerializer
from .serializers import AccountsActiveFlagDetailSerializer
from django.http import Http404
from .permissions import AccountDeactivated


class AccountCreateView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer


class AccountBalanceDetailView(generics.RetrieveAPIView):
    permission_classes = [AccountDeactivated]

    queryset = Account.objects.all()
    serializer_class = AccountsBalanceDetailSerializer

    def get_object(self):
        account_id = self.kwargs.get("pk")
        account = Account.objects.filter(pk=account_id).first()
        if not account:
            raise Http404
        return account


class AccountActiveDetailView(generics.UpdateAPIView):
    permission_classes = [AccountDeactivated]

    queryset = Account.objects.all()
    serializer_class = AccountsActiveFlagDetailSerializer
