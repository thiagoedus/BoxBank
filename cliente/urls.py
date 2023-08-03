from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('cadastrar_conta/', views.cadastrar_conta, name='cadastrar_conta')
]