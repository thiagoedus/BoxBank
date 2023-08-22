from random import randint

def gerar_numero_boleto():
    numero_boleto = ''
    while len(numero_boleto) < 48:
        numero_boleto += str(randint(0, 9))
    return numero_boleto