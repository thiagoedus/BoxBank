from django.shortcuts import render
from .models import CreditCard

def home_credit_card(request):
    if request.method == 'GET':
        return render(request, 'home_credit_card.html')

def request_credit_card(request):
    if request.method == 'GET':
        return render(request, 'credit_card.html')
    elif request.method == 'POST':
        request_limit = request.POST.get('credit-limit')
        conta_user = Conta.objects.get(cliente_id=request.user.get_id)
        if request_limit > conta_user.saldo:
            HttpResponse('Limite supera o saldo da conta')
        else:
            endereco_cobranca = Endereco.objects.get(cliente_id=request.user.get_id)
            credit_card_generated = generators.generate_credit_card()
            credit_card = CreditCard(
                numero_cartao = credit_card_generated['number'],
                validade = credit_card_generated['validade'],
                codigo_seguranca = credit_card_generated['cvv'],
                limite = request_limit,
                emissao = timezone.now,
                endereco_cobranca = endereco_cobranca,
                data_vencimento_fatura = '2023-09-05',
                conta = conta_user
            )
            HttpResponse(f'Parabéns! Seu novo limite é de {request_limit}')