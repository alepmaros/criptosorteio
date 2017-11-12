from django.utils.translation import ugettext as _
from django import forms

from django.template import Template
from material import Layout, Row, Column, Fieldset

from .models import Sorteio

class SorteioForm(forms.ModelForm):

    layout = Layout('nome', 'descricao', 'foto', 'hora_sorteio', 'privacidade')

    class Meta:
        model = Sorteio
        fields = ('nome', 'descricao', 'foto', 'hora_sorteio', 'privacidade' )