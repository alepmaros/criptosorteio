from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Sorteio
from .forms import SorteioForm

class SorteiosListView(LoginRequiredMixin,ListView):
    """
    Classe para listar os sorteios
    """
    login_url = reverse_lazy('login')
    template_name ='sorteios/sorteios.html'
    model = Sorteio
    paginate_by = 10
    
    def get_queryset(self):
        """
        Apenas sorteios publicos e que ainda nao acabaram
        """
        return Sorteio.objects.filter(privacidade='pub').filter(hora_sorteio__gte=timezone.now())

class VisualizarSorteioDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    template_name = 'sorteios/visualizar_sorteio.html'
    model = Sorteio


@login_required
def cadastrar_sorteio(request):

    if request.method == 'POST':
        form = SorteioForm(request.POST, request.FILES)
        if form.is_valid():
            novo_sorteio = form.save(commit=False)
            novo_sorteio.criador_id = request.user.id
            novo_sorteio.save()
            form.save_m2m()

            return HttpResponseRedirect(reverse_lazy('sorteios'))

    else:
        form = SorteioForm()

    return render(request, 'sorteios/criar_sorteio.html', {'form': form})

class DeletarSorteio(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')

class SorteiosCriados(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')

class SorteiosParticipando(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')