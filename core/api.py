from ninja import NinjaAPI
from cliente.api import cliente_router

api = NinjaAPI()

api.add_router('clientes/', cliente_router)