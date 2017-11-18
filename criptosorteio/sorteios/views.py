from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse

from .models import Sorteio
from .forms import SorteioForm

class SorteiosListView(LoginRequiredMixin,ListView):
    """
    Classe para listar os sorteios
    """
    login_url = reverse_lazy('login')
    template_name ='sorteios/sorteios.html'
    model = Sorteio
    paginate_by = 5
    
    def get_queryset(self):
        """
        Apenas sorteios publicos e que ainda nao acabaram
        """
        return Sorteio.objects.filter(privacidade='pub').filter(hora_sorteio__gte=timezone.now())

@login_required
def visualizar_sorteio(request, pk):

    sorteio = get_object_or_404(Sorteio, pk=pk)

    owner = False
    joined = False

    if sorteio.criador.username == request.user.username:
        owner = True

    if sorteio.participantes.filter(pk=request.user.pk).exists():
        joined = True

    return render(request, 'sorteios/visualizar_sorteio.html', {'sorteio': sorteio,
                                                                'owner'  : owner,
                                                                'joined' : joined})

@login_required
def cadastrar_sorteio(request):

    if request.method == 'POST':
        form = SorteioForm(request.POST, request.FILES)
        if form.is_valid():
            novo_sorteio = form.save(commit=False)
            novo_sorteio.criador_id = request.user.id
            novo_sorteio.save()
            form.save_m2m()

            return HttpResponseRedirect(reverse_lazy('visualizar-sorteio', kwargs={'pk':novo_sorteio.pk}))

    else:
        form = SorteioForm()

    return render(request, 'sorteios/criar_sorteio.html', {'form': form})


@login_required
def entrar_sorteio(request, pk):
    get_object_or_404(Sorteio, pk=pk)
    sorteio = Sorteio.objects.get(pk=pk)
    sorteio.participantes.add(request.user)
    sorteio.save()

    return HttpResponseRedirect(reverse_lazy('visualizar-sorteio',  kwargs={'pk':pk}))

@login_required
def sair_sorteio(request, pk):
    get_object_or_404(Sorteio, pk=pk)
    sorteio = Sorteio.objects.get(pk=pk)
    p = sorteio.participantes.remove(request.user)

    return HttpResponseRedirect(reverse_lazy('visualizar-sorteio',  kwargs={'pk':pk}))

@login_required
def deletar_sorteio(request, pk):
    sorteio = get_object_or_404(Sorteio, pk=pk)

    if sorteio.criador.username == request.user.username:
        sorteio.delete()
        return HttpResponseRedirect(reverse_lazy('sorteios'))
    else:
        return HttpResponseRedirect(reverse_lazy('visualizar-sorteio', kwargs={'pk': pk})) 

@login_required
def visualizar_participantes(request, pk):
    sorteio = get_object_or_404(Sorteio, pk=pk)
    participantes = sorteio.participantes.all()

    usuario_participantes = []
    for p in participantes:
        usuario_participantes.append(p.username)

    return JsonResponse({'username':usuario_participantes,
                         'output_value':sorteio.string_nist})

class SorteiosCriados(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')

class SorteiosParticipando(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')