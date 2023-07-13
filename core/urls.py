from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', include('cliente.urls')),
    path('transacoes/', include('transacoes.urls')),
    path('extrato/', include('extrato.urls'))
]
