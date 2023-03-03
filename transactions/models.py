from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator, MaxMoneyValidator


class Transaction(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    valor = MoneyField(
        max_digits=15,
        decimal_places=2,
        default_currency="BRL",
        validators=[
            MinMoneyValidator(0),
            MaxMoneyValidator(999999999999999),
        ],
    )
    dataTransacao = models.DateTimeField(auto_now_add=True)
    conta = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="transactions",
    )
