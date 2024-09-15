from django.urls import path
from . import views

urlpatterns = [
    #path('transacao', views.transacao, 'transacao'),
    path('realizar_emprestimo/', views.realizar_emprestimo, name='realizar_emprestimo'),
    path('tranferencia_pix/', views.tranferencia_pix, name='tranferencia_pix'),
    path('pagar_boleto/', views.pagar_boleto, name='pagar_boleto'),
    #path('confirmar_transferencia/<str:chave_pix>', views.confirmar_transferencia, name='confirmar_transferencia'),
    #path('confirmar_boleto/<str:codigo_boleto>', views.confirmar_boleto, name='confirmar_boleto'),
]