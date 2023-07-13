from django.db import models
from datetime import datetime

class DadosPessoais(models.Model):
    nome_completo = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    email = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.nome_completo

class Endereco(models.Model):
    logradouro = models.CharField(max_length=120)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.logradouro


class Conta(models.Model):
    numero_conta = models.CharField(max_length=12)
    agencia = models.CharField(max_length=6)
    saldo = models.FloatField()
    data_abertura = models.DateField(default=datetime.now())
    status_conta = models.CharField(max_length=12)
    chave_pix = models.CharField(max_length=50)

    def __str__(self):
        return self.numero_conta
    
    def saque(self, valor):
        if self.saldo < valor:
            return
        else:
            self.saldo -= valor
            return valor
        
    def deposito(self, valor):
        if valor > 15000:
            return
        self.saldo += valor
        return valor
    