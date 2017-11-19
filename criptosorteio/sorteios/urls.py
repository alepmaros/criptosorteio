from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SorteiosListView.as_view(), name='sorteios'),
    url(r'^(?P<pk>[0-9a-zA-Z]+)$', views.visualizar_sorteio, name='visualizar-sorteio'),
    url(r'^(?P<pk>[0-9a-zA-Z]+)/entrar/$', views.entrar_sorteio, name='entrar-sorteio'),
    url(r'^(?P<pk>[0-9a-zA-Z]+)/editar/$', views.editar_sorteio, name='editar-sorteio'),
    url(r'^(?P<pk>[0-9a-zA-Z]+)/sair/$', views.sair_sorteio, name='sair-sorteio'),
    url(r'^(?P<pk>[0-9a-zA-Z]+)/deletar/$', views.deletar_sorteio, name='deletar-sorteio'),
    url(r'^(?P<pk>[0-9a-zA-Z]+)/participantes/$', views.visualizar_participantes, name='visualizar-participantes'),
    url(r'^novo/$', views.cadastrar_sorteio, name='novo-sorteio'),
    url(r'^criados/$', views.SorteiosCriados.as_view(), name='sorteios-criados'),
    url(r'^participando/$', views.SorteiosParticipando.as_view(), name='sorteios-participando'),
]