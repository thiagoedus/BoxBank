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

    def __str__(self):
        return self.codigo
    
    @property
    def get_pagador(self):
        return self.pagador
    
    @property
    def get_conta_pagador(self):
        return self.conta_pagador
    
    @get_pagador.setter
    def set_pagador(self, pagador):
        self.pagador = pagador

    @get_conta_pagador.setter
    def set_conta_pagador(self, conta_pagador):
        self.conta_pagador = conta_pagador


