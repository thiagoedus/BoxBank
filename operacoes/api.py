from ninja import Router
from .models import Boleto
from cliente.models import Conta
from django.shortcuts import get_object_or_404

operacoes_router = Router()

@operacoes_router.get('/{codigo_boleto}')
def get_cliente_for_pix(request, codigo_boleto: str):
    boleto = get_object_or_404(Boleto, codigo=codigo_boleto)
    conta_beneficiaria = Conta.objects.get(pk=boleto.conta_beneficiaria.id)
    response = {"valor": boleto.valor, "emissor": conta_beneficiaria.banco, "favorecido":\
                 conta_beneficiaria.cliente.nome_completo}
    return response

#operacoes_router.post
#def pagamento_boleto

# Valor
# Pagador
# Agencia
# Conta

# Favorecido
# Emissor
# Vencimento
