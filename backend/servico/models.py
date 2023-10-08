from django.db import models
from backend.crm.models import Cliente


class Servico(models.Model):
    titulo = models.CharField(
        'titulo',
        max_length=100,
    )

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'servico'
        verbose_name_plural = 'servicos'

    def __str__(self):
        return f'{self.titulo}'


SITUACAO = (
    ('pe', 'Pendente'),
    ('ca', 'Cancelado'),
    ('ap', 'Aprovado'),
    ('an', 'Andamento'),
)


class OrdemServico(models.Model):
    situacao = models.CharField('situacao', max_length=2, choices=SITUACAO)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        verbose_name='cliente',
        related_name='ordem_servicos',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'ordem_servico'
        verbose_name_plural = 'ordens_servico'

    def __str__(self):
        return f'{self.pk}'


class OrdemServicoItem(models.Model):
    ordem_servico = models.ForeignKey(
        OrdemServico,
        on_delete=models.CASCADE,
        verbose_name='ordem_servico',
        related_name='ordem_servico_itens'

    )

    servico = models.ForeignKey(
        Servico,
        on_delete=models.CASCADE,
        verbose_name='servico',
        related_name='ordem_servico_item_servicos'


    )
    valor = models.DecimalField(
        'valor',
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )
    proxima_visita = models.DateTimeField(
        'Próxima Visita', null=True, blank=True)

    class Meta:
        ordering = '-pk',
        verbose_name = 'ordem de servico'
        verbose_name_plural = 'ordens de servico'
