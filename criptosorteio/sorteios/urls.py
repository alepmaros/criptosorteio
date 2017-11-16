from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SorteiosListView.as_view(), name='sorteios'),
    url(r'^(?P<pk>\d+)$', views.visualizar_sorteio, name='visualizar-sorteio'),
    url(r'^(?P<pk>\d+)/entrar/$', views.entrar_sorteio, name='entrar-sorteio'),
    url(r'^(?P<pk>\d+)/deletar/$', views.DeletarSorteio.as_view(), name='deletar-sorteio'),
    url(r'^(?P<pk>\d+)/participantes/$', views.visualizar_participantes, name='visualizar-participantes'),
    url(r'^novo/$', views.cadastrar_sorteio, name='novo-sorteio'),
    url(r'^criados/$', views.SorteiosCriados.as_view(), name='sorteios-criados'),
    url(r'^participando/$', views.SorteiosParticipando.as_view(), name='sorteios-participando'),
]