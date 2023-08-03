from django.shortcuts import render
from cliente.models import Conta
from transacoes.models import Transacao
from django.http import HttpResponse

def realizar_transferencia(request):

    if request.method == 'GET':
        return render(request, 'transacao.html')

    nome_beneficiario = ...
    conta_beneficiario = request.POST.get('conta_beneficiario')
    banco_beneficiario = request.POST.get('banco_beneficiario')
    agencia_beneficiario = request.POST.get('agencia_beneficiario')
    tipo = request.POST.get('tipo')
    cpf_cnpj = ...

    valor_transferencia = request.POST.get('valor_transferencia')


    conta_origem = Conta.objects.get(id=id)
    if not conta_origem.saldo < valor_transferencia:
        return
    
    conta_origem.saque(float(valor_transferencia))

    return HttpResponse("Olá")



def realizar_pix(request):
    chave_pix = request.POST.get('chave_pix_beneficiario')
    valor = request.POST.get('valor_pix')

    conta = Conta.objects.get(chave_pix=chave_pix)

    return

    




    