from ninja import NinjaAPI
from cliente.api import cliente_router
from operacoes.api import operacoes_router

api = NinjaAPI()

api.add_router('clientes/', cliente_router)
api.add_router('operacoes/', operacoes_router)