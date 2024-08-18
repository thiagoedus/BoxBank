from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from . import choices
from decimal import Decimal

class Cliente(AbstractUser):
    nome_completo = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11)
    rg = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=60, unique=True)


    def __str__(self):
        return str(self.username)
    
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
    cep = models.CharField(max_length=15, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.logradouro



class Conta(models.Model):
    numero_conta = models.CharField(max_length=12, unique=True)
    agencia = models.CharField(max_length=6)
    banco = models.CharField(default='0934', max_length=4)
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal(0.00))
    data_abertura = models.DateTimeField(auto_now_add=True)
    status_conta = models.CharField(max_length=20, choices=choices.estados_conta)
    chave_pix = models.CharField(max_length=50, unique=True, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.numero_conta)
    
    def saque(self, valor):
        if self.saldo < Decimal(valor):
            return
        else:
            self.saldo -= Decimal(valor)
            return valor
        
    def deposito(self, valor):
        if Decimal(valor) > 15000:
            return
        self.saldo += Decimal(valor)
        return valor
