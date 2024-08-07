from ninja import ModelSchema, Schema
from .models import Transacao

class TransacaoSchema(ModelSchema):
    class Meta:
        model = Transacao
        exclude = ['id']


class TypeSchema(Schema):
    type: str

class TypeTransacaoSchema(Schema):
    transacao: TransacaoSchema
    type_transacao: TypeSchema