from ninja import Router
from .models import Conta
from django.shortcuts import get_object_or_404
from utils import criptografa_cpf
from django.db import transaction as django_transaction
from transacoes.models import Transacao

cliente_router = Router()

@cliente_router.get('/{chave_pix}')
def get_cliente_for_pix(request, chave_pix: str):
    conta = get_object_or_404(Conta, chave_pix=chave_pix)
    conta.cliente.cpf = criptografa_cpf(conta.cliente.cpf)
    response = {"cpf": conta.cliente.cpf, "banco": conta.banco, "nome":\
                 conta.cliente.nome_completo}
    return response


@cliente_router.post('/{chave_pix}', response={200: dict, 400: dict, 403: dict})
def transaction(request, chave_pix: str, valor):

    payer = get_object_or_404(Conta, cliente__id=request.user.id)
    payee = get_object_or_404(Conta, chave_pix=chave_pix)

    if not payer:
        return 500, {'error': 'Ocorreu um erro na sua conta'}
    
    if not payee:
        return 403, {'error': 'Houve um problema na conta do beneficiário'}
        
    with django_transaction.atomic():
        payer.saque(valor)
        payee.deposito(valor)

        transct = Transacao(
            tipo = transaction.amount,
            conta_origem = payer.id,
            conta_destino = payee.id,
            valor_transacao = valor
        )

        payer.save()
        payee.save()
        transct.save()
    return 200, {"msg": "Transferência com sucesso"}