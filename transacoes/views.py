from django.shortcuts import render
from cliente.models import Conta, Cliente
from .models import Transacao
from django.http import HttpResponse
from operacoes.models import Boleto
from django.utils import timezone
from django.db import transaction as django_transaction
from django.shortcuts import get_object_or_404



# def realizar_transferencia(request):

#     if request.method == 'GET':
#         return render(request, 'transacao.html')

#     nome_beneficiario = ...
#     conta_beneficiario = request.POST.get('conta_beneficiario')
#     banco_beneficiario = request.POST.get('banco_beneficiario')
#     agencia_beneficiario = request.POST.get('agencia_beneficiario')
#     tipo = request.POST.get('tipo')
#     cpf_cnpj = ...

#     valor_transferencia = request.POST.get('valor_transferencia')


#     conta_origem = Conta.objects.get(id=id)
#     if not conta_origem.saldo < valor_transferencia:
#         return
    
#     conta_origem.saque(float(valor_transferencia))

#     return HttpResponse("Olá")


def tranferencia_pix(request):
    if request.method == 'GET':
        conta = Conta.objects.get(cliente__id=request.user.id)        
        print(conta.chave_pix)
        return render(request, 'realizar_pix.html', {'conta': conta})
    elif request.method == 'POST':
        chave_pix = request.POST.get('chave_pix_beneficiario')
        valor = request.POST.get('valor_pix')
        cliente = Cliente.objects.get(id=request.user.id)
        conta_origem = Conta.objects.get(cliente=cliente)
        conta_destino = Conta.objects.get(chave_pix=chave_pix)

        with django_transaction.atomic():
            conta_origem.saque(valor)
            conta_destino.deposito(valor)

            conta_origem.save()
            conta_destino.save()

            transacao = Transacao(tipo='PIX', 
                                conta_origem=conta_origem,
                                conta_destino=conta_destino,
                                valor_transacao=valor
                                )
            
            transacao.save()

        return HttpResponse('Foi')
    
        
def realizar_emprestimo(request):
    if request.method == 'GET':
        return render(request, 'emprestimo.html')


def pagar_boleto(request):
    if request.method == 'GET':
        return render(request, 'pagar_boleto.html')
    elif request.method == 'POST':
        codigo = request.POST.get('codigo_boleto')
        boleto = Boleto.objects.get(codigo=codigo)
        return render(request, 'confirmar_boleto.html', {'boleto': boleto})


def confirmar_boleto(request, codigo_boleto):
    boleto = Boleto.objects.get(codigo=codigo_boleto)
    if boleto.get_situacao == 'PAGO':
        return HttpResponse('O boleto não está aberto')
    
    pagador = Cliente.objects.get(id=request.user.get_id)
    conta_pagador = Conta.objects.get(cliente_id=request.user.get_id)

    conta_beneficiario = Conta.objects.get(id=boleto.conta_beneficiaria_id)

    conta_pagador.saque(boleto.valor)
    conta_beneficiario.deposito(boleto.valor)

    conta_pagador.save()
    conta_beneficiario.save()

    print(pagador.id)
    print(conta_pagador)

    boleto.pagador = pagador
    boleto.conta_pagador = conta_pagador
    boleto.situacao = 'PAGO'

    boleto.data_e_hora_pagamento = timezone.now()

    boleto.save()
    return HttpResponse('foi')

    #TODO Emitir comprovante


def confirmar_transferencia(request):
    conta_origem = Conta.objects.get(id=request.user)
    conta_destino = Conta.objects.get(id=id)
    valor = request.POST.get('valor')
    conta_origem.saque(valor)
    conta_origem.deposito(valor)
    return render(request, 'confirmar_transferencia.html')

    