from django.test import TestCase
from django.urls import reverse

class ClienteURLTest(TestCase):


    def test_url_home_esta_correta(self):
        url_home = reverse('home')
        self.assertEqual(url_home, '/conta/home/')

    def test_url_cadastrar_conta_esta_correta(self):
        url_conta = reverse('cadastrar_conta')
        self.assertEqual(url_conta, '/conta/cadastrar_conta/')

    def test_url_login_esta_correta(self):
        url_conta = reverse('login')
        self.assertEqual(url_conta, '/conta/login/')

    def test_url_logout_esta_correta(self):
        url_conta = reverse('logout')
        self.assertEqual(url_conta, '/conta/logout/')