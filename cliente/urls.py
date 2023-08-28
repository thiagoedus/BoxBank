from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('cadastrar_conta/', views.cadastrar_conta, name='cadastrar_conta'),
    path('request_credit_card/', views.request_credit_card, name='request_credit_card'),
]