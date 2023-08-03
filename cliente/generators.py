from .models import Conta
from random import randint

def gerar_conta():
    conta = Conta.objects.all()
