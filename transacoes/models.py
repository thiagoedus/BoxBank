from django.db import models
from cliente.models import Conta, Cliente
from django.utils import timezone

class Transacao(models.Model):
    data_hora_transacao = models.DateField(default=timezone.now())
    tipo = models.CharField(max_length=15)
    conta_origem = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    conta_destino = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    valor_transacao = models.FloatField()

    def __str__(self):
        return self.tipo