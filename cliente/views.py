from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Cliente, Endereco, Conta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import auth
from . import generators
from django.utils import timezone
from django.shortcuts import get_object_or_404

def redirect_func(request):
    return redirect(reverse('login'))

@login_required(login_url="/conta/login/")
def home(request):
    id_user: int = request.user.get_id
    conta = Conta.objects.get(cliente=id_user)
    user = Cliente.objects.get(id=id_user)
    #if not credit_card:
    return render(request, 'cliente/home.html', {'conta': conta, 'user': user})
    #return render(request, 'home.html', {'conta': conta, 'user': user, 'credit_card': credit_card})

def login_cliente(request):

    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == 'GET':
        return render(request, 'cliente/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse('home'))
        
        return HttpResponse("Usuário inválido")

def logout(request):
    if request.session:
        request.session.flush()
        return redirect(reverse('login'))

def cadastrar_conta(request):
    if request.method == 'GET':
        return render(request, 'cliente/criar_conta.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        rg = request.POST.get('rg')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')
        username = request.POST.get('username')
        password = request.POST.get('senha')

        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')


        cliente = Cliente.objects.create_user(
            username=username,
            nome_completo = nome,
            cpf = cpf,
            telefone = telefone,
            rg = rg,
            email = email,
            password = password
        )

    
        endereco = Endereco(
            logradouro = logradouro,
            numero = numero,
            bairro = bairro,
            cidade = cidade,
            estado = estado,
            cliente = cliente,
        )
        endereco.save()


        num_conta = generators.gerar_conta()
        agencia_conta = generators.gerar_agencia(estado)
        STATUS_CONTA_CRIADA = 'BLOQUEADA'
    
        conta = Conta(
            numero_conta = num_conta,
            agencia = agencia_conta,
            status_conta = STATUS_CONTA_CRIADA,
            cliente = cliente
        )

        conta.save() #TODO bloqueio de conta


        return redirect(reverse('home'))

