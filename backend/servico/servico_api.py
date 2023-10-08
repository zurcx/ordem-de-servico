from typing import List
from backend.servico.models import Servico
from ninja import Router, Schema
from ninja.orm import create_schema

router = Router()

ServicoSchema = create_schema(Servico, fields=(
    'id',
    'titulo',
))


class OrdemServicoItemSchemaIn(Schema):
    ordem_servico_id: int = None
    servico_id: int


class OrdemServicoSchemaIn(Schema):
    situacao: str
    cliente_id: int = None
    ordem_servico_itens: List[OrdemServicoItemSchemaIn]


@router.get('servico/', response=List[ServicoSchema])
def list_servico(request, search=None):
    if search:
        return Servico.objects.filter(titulo__istartswith=search)
    return Servico.objects.all()
