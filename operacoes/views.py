from django.shortcuts import render
from . import generators, utils
from cliente.models import Cliente, Conta, Endereco
from datetime import datetime
from .models import Boleto
from django.http import HttpResponse

def boleto(request):
    return render(request, 'boleto.html')

def gerar_boleto(request):
    if request.method == 'GET':
        return render(request, 'gerar_boleto.html')
    elif request.method == 'POST':
        numero_boleto = generators.gerar_numero_boleto()
        beneficiario = Cliente.objects.get(id=request.user.get_id)
        conta_beneficiario = Conta.objects.get(cliente=beneficiario)
        data_hora_processamento = datetime.now()
        vencimento = '2023-12-12'
        situacao = 'ABERTO'
        valor = float(request.POST.get('valor_boleto'))

        boleto = Boleto(
                codigo = numero_boleto,
                beneficiario = beneficiario,
                conta_beneficiaria = conta_beneficiario,
                data_e_hora_processamento = data_hora_processamento,
                vencimento = vencimento,
                situacao = situacao,
                valor = valor,
        )

        boleto.save()

        endereco_beneficiario = Endereco.objects.get(cliente=request.user.id)

        return render(request, 'boleto.html', {'beneficiario': beneficiario, 'conta_beneficiario': conta_beneficiario, 'boleto': boleto, 'endereco_beneficiario': endereco_beneficiario})
    
        
