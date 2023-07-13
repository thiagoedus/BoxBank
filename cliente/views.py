from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DadosPessoais, Endereco, Conta

def home(request):
    return HttpResponse('Olá mundo')

def cadastrar_conta(request):
    if request.method == 'GET':
        ...
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        rg = request.POST.get('rg')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')

        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        try:
            cliente = DadosPessoais(
                nome_completo = nome,
                cpf = cpf,
                telefone = telefone,
                rg = rg,
                email = email,
                data_nascimento = data_nascimento,
                senha = ...
            )

            endereco = Endereco(
                logradouro = logradouro,
                numero = numero,
                bairro = bairro,
                cidade = cidade,
                estado = estado,
                cliente = cliente,
            )
        except:
            print('Erro encontrado')



        return redirect('home')




