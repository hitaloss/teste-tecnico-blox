from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator, MaxMoneyValidator


class Account(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    id_pessoa = models.PositiveIntegerField(unique=True)
    saldo = MoneyField(
        max_digits=15,
        decimal_places=2,
        default_currency="BRL",
        validators=[
            MinMoneyValidator(0),
            MaxMoneyValidator(999999999999999),
        ],
    )
    limite_saque_diario = MoneyField(
        max_digits=15,
        decimal_places=2,
        default_currency="BRL",
        validators=[
            MinMoneyValidator(0),
            MaxMoneyValidator(3000),
        ],
    )
    flag_ativo = models.BooleanField(default=True)
    tipo_conta = models.IntegerField(default=1)
    data_criacao = models.DateTimeField(auto_now_add=True)
