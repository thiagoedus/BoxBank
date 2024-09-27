from django.db import models
from cliente.models import Conta
from decimal import Decimal

class ComprovantePIX(models.Model):
    conta_pagador = models.ForeignKey(Conta, related_name="conta_pagador", on_delete=models.DO_NOTHING, editable=False)
    conta_beneficiario = models.ForeignKey(Conta, related_name="conta_beneficiario", on_delete=models.DO_NOTHING, editable=False)
    data_hora_transacao = models.DateTimeField(auto_now_add=True, editable=False)
    banco_pagador = models.CharField(max_length=10, default="0934", editable=False)
    banco_beneficiario = models.CharField(max_length=10, default="0", editable=False)
    valor = amount = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal(0.00), editable=False, editable=False)   
    chave_pix = models.CharField(max_length=255, editable=False)