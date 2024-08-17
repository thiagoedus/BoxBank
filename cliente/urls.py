from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_func, name='init'),
    path('login/', views.login_cliente, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('cadastrar_conta/', views.cadastrar_conta, name='cadastrar_conta'),
]