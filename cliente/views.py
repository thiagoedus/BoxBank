from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Cliente, Endereco, Conta
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from . import generators


@login_required(login_url="/conta/login/")
def home(request):
    id_user: int = request.user.get_id
    print(id_user)
    conta = Conta.objects.get(cliente=id_user)
    user = Cliente.objects.get(id=id_user)
    print(conta.numero_conta)
    return render(request, 'home.html', {'conta': conta, 'user': user})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if user is None:
            return HttpResponse("Um erro foi encontrado")
        
        auth.login(request, user)
        return redirect(reverse('home'))

def logout(request):
    if request.session:
        request.session.flush()
        return redirect(reverse('login'))

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
        username = 'thiagohenriq'
        password = '123456'

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

