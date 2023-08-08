from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('cadastrar_conta/', views.cadastrar_conta, name='cadastrar_conta'),
    path('realizar_emprestimo/', views.realizar_emprestimo, name='realizar_emprestimo'),
    path('tranferencia_pix/', views.tranferencia_pix, name='tranferencia_pix'),
    path('pagar_boleto/', views.pagar_boleto, name='pagar_boleto'),
    path('confirmar_transferencia/<str:chave_pix>', views.confirmar_transferencia, name='confirmar_transferencia')
]