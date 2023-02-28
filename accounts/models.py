from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import AbstractUser

class Account(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    id_pessoa = models.IntegerField(unique=True, editable=False)
    saldo = MoneyField(max_digits=15, decimal_places=2)
    limite_saque_diario = MoneyField(max_digits=15, decimal_places=2)
    flag_ativo = models.BooleanField(default=True)
    tipo_conta = models.IntegerField(default=1)
    data_criacao = models.DateTimeField(auto_now_add=True)
