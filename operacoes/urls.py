from django.urls import path
from . import views

urlpatterns = [
    path('boleto/', views.boleto, name='boleto'),
    path('gerar_boleto/', views.gerar_boleto, name='gerar_boleto'),
]