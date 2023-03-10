from rest_framework import serializers
from rest_framework import generics
from .models import Transaction
from .serializers import TransactionsSerializer
from accounts.models import Account
from djmoney.money import Money
from django.http import Http404


from .permissions import AccountDeactivated


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionsSerializer

    def get_queryset(self):
        account_id = self.kwargs.get("pk")
        return Transaction.objects.filter(conta_id=account_id)


class DepositView(generics.CreateAPIView):
    serializer_class = TransactionsSerializer
    queryset = Transaction.objects.all()
    permission_classes = [AccountDeactivated]

    def perform_create(self, serializer):
        account_id = self.kwargs.get("pk")
        amount = serializer.validated_data["valor"]
        transaction = Transaction.objects.create(valor=amount, conta_id=account_id)
        try:
            account = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            raise Http404("Account matching query does not exist.")
        account.saldo = account.saldo + Money(amount, "BRL")
        account.save()
        return transaction


class WithdrawView(generics.CreateAPIView):
    serializer_class = TransactionsSerializer
    queryset = Transaction.objects.all()
    permission_classes = [AccountDeactivated]

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
