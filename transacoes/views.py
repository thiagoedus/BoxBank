from django.shortcuts import render
from cliente.models import Conta
from transacoes.models import Transacao, Beneficiario

def realizar_transferencia(request, id):

    nome_beneficiario = ...
    conta_beneficiario = request.POST.get('conta_beneficiario')
    banco_beneficiario = request.POST.get('banco_beneficiario')
    agencia_beneficiario = request.POST.get('agencia_beneficiario')
    tipo = request.POST.get('tipo')
    cpf_cnpj = ...

    valor_transferencia = request.POST.get('valor_transferencia')


    beneficiario = Beneficiario(
    nome_beneficiario = nome_beneficiario,
    conta_beneficiario = conta_beneficiario,
    agencia_beneficiario = agencia_beneficiario,
    banco = banco_beneficiario,
    tipo_conta = tipo,
    cpf_cnpj = cpf_cnpj
    )

    beneficiario.save()

    conta_origem = Conta.objects.get(id=id)
    if not conta_origem.saldo < valor_transferencia:
        return
    
    conta_origem.saque(float(valor_transferencia))

    if beneficiario.banco == '9748':
        beneficiario.receber_tranferencia(float(valor_transferencia))

    return



def realizar_pix(request, id):
    chave_pix = request.POST.get('chave_pix_beneficiario')
    nome_beneficiario = ...
    conta_beneficiario = request.POST.get('conta_beneficiario')
    banco_beneficiario = request.POST.get('banco_beneficiario')
    agencia_beneficiario = request.POST.get('agencia_beneficiario')
    tipo = request.POST.get('tipo')
    cpf_cnpj = ...