from django.db import models
from cliente.models import Cliente, Conta
from django.utils import timezone

class Boleto(models.Model):
    codigo = models.CharField(max_length=48, unique=True)
    beneficiario = models.ForeignKey(Cliente, related_name='beneficiario', on_delete=models.DO_NOTHING)
    conta_beneficiaria = models.ForeignKey(Conta, related_name='conta_beneficiario', on_delete=models.DO_NOTHING)
    data_e_hora_processamento = models.DateTimeField(default=timezone.now)
    vencimento = models.DateField()
    valor = models.FloatField(default=0)
    situacao = models.CharField(max_length=12)
    pagador = models.ForeignKey(Cliente, related_name='pagador', on_delete=models.DO_NOTHING, null=True, blank=True)
    conta_pagador = models.ForeignKey(Conta, related_name='conta_pagador', on_delete=models.DO_NOTHING, null=True, blank=True)
    data_e_hora_pagamento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.codigo
    
    @property
    def get_situacao(self):
        return self.situacao
    
    @get_situacao.setter
    def set_situacao(self, situacao: str) -> None:
        if self.get_situacao() == 'ABERTO':
            self.situacao = situacao



