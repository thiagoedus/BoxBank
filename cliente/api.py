from ninja import Router, Schema
from .models import Conta
from django.shortcuts import get_object_or_404
from utils import criptografa_cpf
from django.db import transaction as django_transaction
from transacoes.models import Transacao


# TODO alterar para class Decimal
class SaldoSchema(Schema):
    saldo: float

# TODO alterar para class Decimal
class DadosPixSchema(Schema):
    valor: float
    chave_pix: str

cliente_router = Router()


@cliente_router.get('/verificar-saldo-cliente')
def get_cliente_for_pix(request):
    conta = get_object_or_404(Conta, cliente__id=request.user.id)
    return {"saldo_cliente": conta.saldo}

@cliente_router.post('/verificar-saldo', response={200: dict, 400: dict, 403: dict, 422: dict})
def get_cliente_for_pix(request, valor: SaldoSchema):
    conta = get_object_or_404(Conta, cliente__id=request.user.id)
    if not valor.saldo or not isinstance(valor.saldo, float):
        return {"code": 0, "msg": "Ocorreu um erro, verifique os dados e tente novamente"}
    if valor.saldo <= 0.0:
        return {"code": 0, "msg": 'O valor não pode ser negativo'}
    if valor.saldo > float(conta.saldo):
        return {"code": 0, "msg": "Saldo insuficiente"}
    return {"code": 1}

@cliente_router.post('/realizar-pix', response={200: dict, 400: dict, 403: dict, 422: dict})
def get_cliente_for_pix(request, dados_pix: DadosPixSchema):
    conta = get_object_or_404(Conta, cliente__id=request.user.id)
    if not dados_pix.valor or dados_pix.valor == 0:
        return 403, {"msg": "Valor inválido"}
    if dados_pix.valor > conta.saldo:
        return 400, {"msg": "Saldo insuficiente"}
    conta_beneficiaria = get_object_or_404(Conta, chave_pix=dados_pix.chave_pix)

    with django_transaction.atomic():
        conta.saque(dados_pix.valor)
        conta_beneficiaria.deposito(dados_pix.valor)
        conta.save()
        conta_beneficiaria.save()
    
    return 200, {"msg": "ok"}


# @cliente_router.post('/{chave_pix}', response={200: dict, 400: dict, 403: dict})
# def transaction(request, chave_pix: str, valor):

#     payer = get_object_or_404(Conta, cliente__id=request.user.id)
#     payee = get_object_or_404(Conta, chave_pix=chave_pix)

#     if not payer:
#         return 500, {'error': 'Ocorreu um erro na sua conta'}
    
#     if not payee:
#         return 403, {'error': 'Houve um problema na conta do beneficiário'}
        
#     with django_transaction.atomic():
#         payer.saque(valor)
#         payee.deposito(valor)

#         transct = Transacao(
#             tipo = transaction.amount,
#             conta_origem = payer.id,
#             conta_destino = payee.id,
#             valor_transacao = valor
#         )

#         payer.save()
#         payee.save()
#         transct.save()
#     return 200, {"msg": "Transferência com sucesso"}