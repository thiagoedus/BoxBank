from .models import Conta
from random import randint

def gerar_conta():
    conta = Conta.objects.all()
    conta_cliente = ''
    while len(conta_cliente) < 8:
        conta_cliente = str(randint(0, 9))
    if conta_cliente in conta:
        gerar_conta()
    return conta_cliente

def gerar_agencia(estado):
    estados = {
        "AC": "1811",
        "AL": "1960",
        "AP": "1077",
        "AM": "1280",
        "BA": "1453",
        "CE": "1226",
        "DF": "1882",
        "ES": "1239",
        "GO": "1738",	
        "MA": "1108",
        "MT": "1362",
        "MS": "1267",
        "MG": "1558",
        "PA": "1741",
        "PB": "1532",
        "PR": "1141",
        "PE": "1743",
        "PI": "1763",
        "RJ": "1776",
        "RN": "1747",
        "RS": "1314",
        "RO": "1970",
        'RR': "1017",
        "SC": "1614",
        "SP": '1654',
        "SE": '1344',
        "TO": "1290",
    }

    estado_ag = estados['estado']
    if estado_ag:
        return estado_ag
