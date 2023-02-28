from rest_framework import generics
from .models import Account
from .serializers import AccountsSerializer


class AccountCreateView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer

class AccountBalanceDetailView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer

    def get_object(self):
        account_id = self.kwargs.get("pk")
        return Account.objects.filter(pk=account_id).values("saldo").first()
