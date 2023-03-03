from rest_framework import serializers
from rest_framework import generics
from .models import Transaction
from .serializers import TransactionsSerializer
from accounts.models import Account
from djmoney.money import Money

# from .permissions import AccountDeactivated


class DepositView(generics.CreateAPIView):
    serializer_class = TransactionsSerializer
    queryset = Transaction.objects.all()

    def perform_create(self, serializer):
        account_id = self.kwargs.get("pk")
        amount = serializer.validated_data["valor"]
        transaction = Transaction.objects.create(valor=amount, conta_id=account_id)
        account = Account.objects.get(id=account_id)
        account.saldo = account.saldo + Money(amount, "BRL")
        account.save()
        return transaction


class WithdrawView(generics.CreateAPIView):
    serializer_class = TransactionsSerializer
    queryset = Transaction.objects.all()

    def perform_create(self, serializer):
        account_id = self.kwargs.get("pk")
        amount = serializer.validated_data["valor"]
        account = Account.objects.get(id=account_id)
        if account.saldo < Money(amount, "BRL"):
            response_data = {"detail": "Insufficient funds."}
            raise serializers.ValidationError(response_data)
        new_transaction = Transaction.objects.create(valor=-amount, conta_id=account_id)
        account.saldo = account.saldo - Money(amount, "BRL")
        account.save()
        return new_transaction
