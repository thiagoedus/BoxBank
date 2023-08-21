from django.db import models
from cliente.models import Cliente, Conta
from django.utils import timezone

class boleto(models.Model):
    codigo = models.CharField(max_length=48, unique=True)
    beneficiario = models.ForeignKey(Cliente, related_name='beneficiario', on_delete=models.DO_NOTHING)
    conta_beneficiaria = models.ForeignKey(Conta, related_name='conta_beneficiario', on_delete=models.DO_NOTHING)
    data_e_hora_processamento = models.DateTimeField(default=timezone.now)
    vencimento = models.DateField()
    situacao = models.CharField(max_length=12)
    pagador = models.ForeignKey(Cliente, related_name='pagador', on_delete=models.DO_NOTHING)
    conta_pagador = models.ForeignKey(Conta, related_name='conta_pagador', on_delete=models.DO_NOTHING)



