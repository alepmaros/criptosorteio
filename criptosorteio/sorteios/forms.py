from django.utils.translation import ugettext as _
from django import forms
from django.utils import timezone

from django.template import Template
from material import Layout, Row, Column, Fieldset

from .models import Sorteio

class SorteioForm(forms.ModelForm):

    layout = Layout('nome', 'descricao', 'foto', 'hora_sorteio', 'privacidade')

    class Meta:
        model = Sorteio
        fields = ('nome', 'descricao', 'foto', 'hora_sorteio', 'privacidade' )

    def clean_hora_sorteio(self):
        hora_sorteio = self.cleaned_data.get('hora_sorteio')
        if hora_sorteio < timezone.now():
            raise forms.ValidationError(_('Sorteio não pode ser no passado'))
        return hora_sorteio