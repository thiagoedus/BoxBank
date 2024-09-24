from ninja import Router
from cliente.models import Conta
from django.shortcuts import get_object_or_404
from utils import criptografa_cpf
from .schemas import TransacoesSchema

transactions_router = Router()

# @transactions_roter.post('/', response={200: dict, 400: dict, 500: dict})
# def get_datos_transacao(request):
#     transacao = transacao.objects.all()
#     response = [{"id": u.id, "username": u.username, "first_name": u.first_name\
#                  , "last_name": u.last_name, "cpf": u.cpf, "email": u.email, "amount": u.amount\
#                     } for u in users]
#     return response

@transactions_router.post('/pagamentos/pix', response={200: dict, 400: dict, 500: dict})
def get_dados_por_chave_pix(request, transacao: TransacoesSchema):
        conta = get_object_or_404(Conta, chave_pix=transacao.chave_pix)
        conta.cliente.cpf = criptografa_cpf(conta.cliente.cpf)
        response = {"cpf": conta.cliente.cpf, "banco": conta.banco, "nome":\
                    conta.cliente.nome_completo}
        return response

@transactions_router.post('/pagamentos/pix/pagar', response={200: dict, 400: dict, 500: dict})
def realizar_pagamento(request, transacao: TransacoesSchema):
        conta = get_object_or_404(Conta, chave_pix=transacao.chave_pix)
        
        return response