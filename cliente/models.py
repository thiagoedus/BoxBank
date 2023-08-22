from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Cliente(AbstractUser):
    nome_completo = models.CharField(max_length=60, null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=11, null=True, blank=True)
    rg = models.CharField(max_length=10, unique=True, null=True, blank=True)
    email = models.CharField(max_length=60, unique=True, null=True, blank=True)


    def __str__(self):
        return str(self.nome_completo)
    
    @property
    def get_id(self):
        return self.id
    
    @property
    def get_name(self):
        return self.nome_completo

class Endereco(models.Model):
    logradouro = models.CharField(max_length=120)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.logradouro



class Conta(models.Model):
    numero_conta = models.CharField(max_length=12, unique=True)
    agencia = models.CharField(max_length=6)
    banco = models.CharField(default='0934', max_length=4)
    saldo = models.FloatField(default=0)
    data_abertura = models.DateField(default=datetime.now())
    status_conta = models.CharField(max_length=12)
    chave_pix = models.CharField(max_length=50, unique=True, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.numero_conta)
    
    def saque(self, valor):
        if self.saldo < float(valor):
            return
        else:
            self.saldo -= float(valor)
            return valor
        
    def deposito(self, valor):
        if float(valor) > 15000:
            return
        self.saldo += float(valor)
        return valor
    

class CreditCard(models.Model):
    numero_cartao = models.CharField(max_length=16, unique=True)
    validade = models.DateField()
    codigo_seguranca = models.CharField(max_length=3)
    bandeira = models.CharField(max_length=4, default='MC')
    limite = models.FloatField()
    limite_usado = models.FloatField(default=0)
    emissao = models.DateField()
    endereco_cobranca = models.CharField(max_length=12)
    status = models.CharField(max_length=12, default='BLOQUEADO')
    tipo = models.CharField(max_length=15)
    data_vencimento_fatura = models.DateField()

    def __str__(self):
        return self.numero_cartao
    
    def limite_disponivel(self):
        return self.limite - self.limite_usado
    
    def comprar(self, valor):
        if float(valor) > self.limite_disponivel():
            return None
        else:
            self.limite_usado += valor