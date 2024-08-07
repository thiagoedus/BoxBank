from ninja import Router
from .schemas import TypeTransacaoSchema

transactions_roter = Router()

@transactions_roter.post('/', response={200: dict, 400: dict, 500: dict})
def get_datos_transacao(request):
    transacao = transacao.objects.all()
    response = [{"id": u.id, "username": u.username, "first_name": u.first_name\
                 , "last_name": u.last_name, "cpf": u.cpf, "email": u.email, "amount": u.amount\
                    } for u in users]
    return response