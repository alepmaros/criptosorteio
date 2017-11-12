from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Sorteios(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'sorteios/sorteios.html'

class VisualziarSorteio(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')

class DeletarSorteio(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')

class NovoSorteio(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')

class SorteiosCriados(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')

class SorteiosParticipando(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')