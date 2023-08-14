from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Cliente, Endereco, Conta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

@login_required(login_url="/conta/login")
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if not user:
            return HttpResponse('Login inválido')
            #TODO mensagem personalizada

        
        login_django(request, user)
        return redirect(reverse('home'))


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
        username = 'thiagoedus'
        password = '123'

        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')


        cliente = Cliente(
            username=username,
            nome_completo = nome,
            cpf = cpf,
            telefone = telefone,
            rg = rg,
            email = email,
            data_nascimento = data_nascimento,
            password = password
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
    contas = Conta.objects.all()
    return render(request, 'tranferencia_pix.html', {'contas': contas})

def pagar_boleto(request):
    return render(request, 'pagar_boleto.html')

def confirmar_transferencia(request, chave_pix):
    conta_origem = Conta.objects.get(id=request.user)
    conta_destino = Conta.objects.get(id=id)
    valor = request.POST.get('valor')
    conta_origem.saque(valor)
    conta_origem.deposito(valor)
    return render(request, 'confirmar_transferencia.html')