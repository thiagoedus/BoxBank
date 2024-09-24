from ninja import Router
from .models import Boleto
from cliente.models import Conta
from django.shortcuts import get_object_or_404
from django.db import transaction as django_transaction

operacoes_router = Router()

@operacoes_router.get('/{codigo_boleto}')
def get_cliente_for_boleto(request, codigo_boleto: str):
    boleto = get_object_or_404(Boleto, codigo=codigo_boleto)
    conta_beneficiaria = Conta.objects.get(pk=boleto.conta_beneficiaria.id)
    response = {"valor": boleto.valor, "emissor": conta_beneficiaria.banco, "favorecido":\
                 conta_beneficiaria.cliente.nome_completo}
    return 200, response

@operacoes_router.get('/{codigo_boleto}/pagar')
def pagar_boleto(request, codigo_boleto: str):
    boleto = get_object_or_404(Boleto, codigo=codigo_boleto)
    conta_beneficiaria = get_object_or_404(Conta, pk=boleto.conta_beneficiaria.id)
    conta_pagador = get_object_or_404(Conta, pk=request.user.id)
    if not boleto or not conta_beneficiaria or not conta_pagador:
        return 403, {"error": "Ocorreu um erro com os dados"}
    if conta_pagador.saldo < boleto.valor:
        return 400, {"error": "Saldo insuficiente"}
    with django_transaction.atomic():
        conta_pagador.saque(boleto.valor)
        conta_beneficiaria.deposito(boleto.valor)
        boleto.situacao = 'PAGO'
        conta_pagador.save()
        conta_beneficiaria.save()
        boleto.save()

    return 200, {"msg": "Success"}

#operacoes_router.post
#def pagamento_boleto

# Valor
# Pagador
# Agencia
# Conta

# Favorecido
# Emissor
# Vencimento
