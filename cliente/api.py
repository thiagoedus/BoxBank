from ninja import Router
from .models import Conta
from django.shortcuts import get_object_or_404

cliente_router = Router()

@cliente_router.get('/{chave_pix}')
def get_cliente_for_pix(request, chave_pix: str):
    conta = get_object_or_404(Conta, chave_pix=chave_pix)
    response = {"cpf": conta.cliente.cpf, "banco": conta.banco, "nome":\
                 conta.cliente.nome_completo}
    return response