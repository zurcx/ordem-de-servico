from django import forms
from django.forms.fields import DateInput
from .models import OrdemServico

class OrdemServicoForm(forms.ModelForm):
    servico = forms.CharField()
    valor = forms.DecimalField()
    proxima_visita = forms.DateField(
        label='Próxima Visita',
        required=False,
        widget=DateInput(
            format="%Y-%m-%d",
            attrs={
                'type': 'date',
                'class': 'form-control'
        }),
        input_formats=('%Y-%m-%d',),
    )

    class Meta:
        model = OrdemServico
        fields = ('situacao',) 
