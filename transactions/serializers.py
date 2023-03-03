from rest_framework import serializers
from djmoney.contrib.django_rest_framework import MoneyField
from .models import Transaction


class TransactionsSerializer(serializers.ModelSerializer):
    valor = MoneyField(max_digits=10, decimal_places=2)

    class Meta:
        model = Transaction
        fields = ["id", "valor", "dataTransacao"]
        read_only_fields = ["id", "dataTransacao"]
        depth = 1
