from django.contrib import admin
from .models import DadosPessoais, Endereco, Conta

admin.site.register(DadosPessoais)
admin.site.register(Endereco)
admin.site.register(Conta)