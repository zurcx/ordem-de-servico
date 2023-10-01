from typing import List
from backend.servico.models import Servico
from ninja import Router 
from ninja.orm import create_schema

router = Router()

ServicoSchema = create_schema(Servico)

@router.get('servico/', response=List[ServicoSchema])
def list_servico(request, search=None):
    if search:
        ...
    return Servico.objects.all()

