from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class SorteiosView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'sorteios/sorteios.html'
