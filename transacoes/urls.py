from django.urls import path
from . import views

urlpatterns = [
    #path('transacao', views.transacao, 'transacao'),
    path('realizar_transferencia', views.realizar_transferencia, name='realizar_tranferencia'),
    path('realizar_pix', views.realizar_pix, name='realizar_pix')

]