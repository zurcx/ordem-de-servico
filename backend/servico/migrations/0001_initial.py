# Generated by Django 4.2.5 on 2023-09-24 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.CharField(choices=[('pe', 'Pendente'), ('ca', 'Cancelado'), ('ap', 'Aprovado'), ('an', 'Andamento')], max_length=2, verbose_name='situacao')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ordem_servicos', to='crm.cliente', verbose_name='cliente')),
            ],
            options={
                'verbose_name': 'ordem_servico',
                'verbose_name_plural': 'ordens_servico',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='titulo')),
            ],
            options={
                'verbose_name': 'servico',
                'verbose_name_plural': 'servicos',
                'ordering': ('titulo',),
            },
        ),
        migrations.CreateModel(
            name='OrdemServicoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='valor')),
                ('proxima_visita', models.DateTimeField(blank=True, null=True, verbose_name='Próxima Visita')),
                ('ordem_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordem_servico_item', to='servico.ordemservico', verbose_name='ordem_servico')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordem_servico_item_servicos', to='servico.servico', verbose_name='servico')),
            ],
            options={
                'verbose_name': 'ordem de servico',
                'verbose_name_plural': 'ordens de servico',
                'ordering': ('-pk',),
            },
        ),
    ]
