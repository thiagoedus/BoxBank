from django.test import TestCase
from django.urls import reverse, resolve
from cliente import views

class ClienteViewTest(TestCase):




    def test_cliente_home_funcao_view_esta_correta(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, views.home)

    # Teste de requisição HTTP

    def test_cliente_home_retorna_302_se_nao_logado(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

    def test_cliente_pagina_login_retorna_200(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_cliente_pagina_logout_retorna_302(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_cliente_pagina_cadastro_conta_retorna_200(self):
        response = self.client.get(reverse('cadastrar_conta'))
        self.assertEqual(response.status_code, 200)

    # Teste de Templates

    # TODO criar a Cliente Base de testes  
    # def test_cliente_template_home_esta_carregado(self):
    #     response = self.client.get(reverse('cadastrar_conta'))
    #     self.assertTemplateUsed(response, 'cliente/criar_conta.html')

    def test_cliente_template_cadastrar_conta_esta_carregado(self):
        response = self.client.get(reverse('cadastrar_conta'))
        self.assertTemplateUsed(response, 'cliente/criar_conta.html')

    def test_cliente_template_login_esta_carregado(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'cliente/login.html')
    