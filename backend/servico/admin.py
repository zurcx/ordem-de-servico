from django.contrib import admin
from .models import Servico, OrdemServico, OrdemServicoItem

admin.site.register(Servico)
admin.site.register(OrdemServico)
admin.site.register(OrdemServicoItem)
