from django.db import models
from datetime import datetime
from cliente.models import Conta

class Beneficiario(models.Model):
    nome_beneficiario = models.CharField(max_length=50)
    conta_beneficiario = models.CharField(max_length=10)
    agencia_beneficiario = models.CharField(max_length=10)
    banco = models.CharField(max_length=20)
    tipo_conta = models.CharField(max_length=2)
    cpf_cnpj = models.CharField(max_length=22)
    chave_pix = models.CharField(max_length=50, null=True, blank=True)
    conta = models.ForeignKey(Conta, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.nome_beneficiario
    
    def receber_tranferencia(self, valor):
        self.conta.saldo += valor

class Transacao(models.Model):
    data_hora_transacao = models.DateField(default=datetime.now())
    tipo = models.CharField(max_length=15)
    conta_origem = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    conta_destino = models.ForeignKey(Beneficiario, on_delete=models.DO_NOTHING)
    valor_transacao = models.FloatField()

    def __str__(self):
        return self.tipo