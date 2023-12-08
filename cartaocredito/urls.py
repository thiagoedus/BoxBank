from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_credit_card, name='home_credit_card')
]