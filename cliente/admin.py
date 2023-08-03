from django.contrib import admin
from .models import Cliente, Endereco, Conta

admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Conta)