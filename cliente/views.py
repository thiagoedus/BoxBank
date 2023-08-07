from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Endereco, Conta

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def cadastrar_conta(request):
    if request.method == 'GET':
        return render(request, 'criar_conta.html')
    
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


        cliente = Cliente(
            nome_completo = nome,
            cpf = cpf,
            telefone = telefone,
            rg = rg,
            email = email,
            data_nascimento = data_nascimento
        )

        cliente.save()

    
        endereco = Endereco(
            logradouro = logradouro,
            numero = numero,
            bairro = bairro,
            cidade = cidade,
            estado = estado,
            cliente = cliente,
        )
        endereco.save()

        

        
        

        return redirect('home')

def realizar_emprestimo(request):
    if request.method == 'GET':
        return render(request, 'emprestimo.html')


def tranferencia_pix(request):
    return render(request, 'tranferencia_pix.html')

def pagar_boleto(request):
    return render(request, 'pagar_boleto.html')