from django.test import TestCase
from cliente.models import Cliente, Conta, Endereco


class ClienteTestBase(TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def cria_cliente(
        self,
        nome_completo='Usuario Nome Teste',
        password='senha123',
        username='usernameteste',
        cpf='45394790086',
        telefone='45999674312',
        rg='SP90743278',
        email='teste@gmail.com'
    ):
        return Cliente.objects.create_user(
            username=username,
            password=password,
            nome_completo=nome_completo,
            cpf=cpf,
            telefone=telefone,
            rg=rg,
            email=email
        )

    def cria_endereco(
        self,
        logradouro = 'Rua Teste',
        numero = 340,
        bairro = 'Bairro Teste',
        cidade = 'Cidade Teste',
        estado = 'TE',
        cep = '00000000',
        tipo = 'Casa'
    ):
        return Endereco.objects.create(
            logradouro = logradouro,
            numero = numero,
            bairro = bairro,
            cidade = cidade,
            estado = estado,
            cep = cep,
            cliente = self.cria_cliente(),
            tipo = tipo
        )
    
    def cria_conta(
            self,
            numero_conta = '00000000',
            agencia = '0000',
            banco = '0000',
            saldo = 0.0,
            status_conta = 'Ativa',
            chave_pix = '00000'
                   ):
        
        return Conta.objects.create(
            numero_conta = numero_conta,
            agencia = agencia,
            banco = banco,
            saldo = saldo,
            status_conta = status_conta,
            chave_pix = chave_pix,
            cliente = self.cria_cliente(),
        )