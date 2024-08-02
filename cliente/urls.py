from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_cliente, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('cadastrar_conta/', views.cadastrar_conta, name='cadastrar_conta'),
]