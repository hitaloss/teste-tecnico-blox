from rest_framework import serializers
from .models import Account


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=["id_pessoa", "saldo", "limite_saque_diario", "flag_ativo", "tipo_conta", "data_criacao"]
        read_only_fields=["id_pessoa", "data_criacao"]
    
    def create(self, validated_data):
        last_person = Account.objects.order_by("id_pessoa").last()
        if not last_person:
            validated_data["id_pessoa"] = 1
        else:
            validated_data["id_pessoa"] = last_person.id_pessoa + 1
        return super().create(validated_data)
