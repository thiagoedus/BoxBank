from django.db import models
from cliente.models import Conta

class CreditCard(models.Model):
    numero_cartao = models.CharField(max_length=16, unique=True)
    validade = models.DateField()
    codigo_seguranca = models.CharField(max_length=3)
    bandeira = models.CharField(max_length=4, default='MC')
    limite = models.FloatField(default=0)
    limite_usado = models.FloatField(default=0)
    emissao = models.DateField()
    endereco_cobranca = models.CharField(max_length=12)
    status = models.CharField(max_length=12, default='BLOQUEADO')
    tipo = models.CharField(max_length=15)
    data_vencimento_fatura = models.DateField()
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.numero_cartao
    
    def limite_disponivel(self):
        return self.limite - self.limite_usado
    
    def comprar(self, valor):
        if float(valor) > self.limite_disponivel():
            return None
        else:
            self.limite_usado += valor