from rest_framework import serializers
from djmoney.contrib.django_rest_framework import MoneyField
from .models import Account
from .exceptions import ConflictError


class AccountsSerializer(serializers.ModelSerializer):
    saldo = MoneyField(max_digits=10, decimal_places=2)
    limite_saque_diario = MoneyField(max_digits=10, decimal_places=2)

    class Meta:
        model = Account
        fields = [
            "id_pessoa",
            "saldo",
            "limite_saque_diario",
            "flag_ativo",
            "tipo_conta",
            "data_criacao",
        ]
        read_only_fields = ["data_criacao"]

    def create(self, validated_data):
        id_pessoa = validated_data["id_pessoa"]
        obj, created = Account.objects.get_or_create(
            defaults=validated_data, id_pessoa=id_pessoa
        )
        if not created:
            raise ConflictError({"id_pessoa": ["This id_person already exists."]})
        return obj


class AccountsBalanceDetailSerializer(serializers.ModelSerializer):
    saldo = MoneyField(max_digits=10, decimal_places=2)

    class Meta:
        model = Account
        fields = ["saldo"]


class AccountsActiveFlagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["flag_ativo"]
