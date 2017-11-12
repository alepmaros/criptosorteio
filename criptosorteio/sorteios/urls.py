from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Sorteios.as_view(), name='sorteios'),
    url(r'^(?P<pk>\d+)/$', views.VisualziarSorteio.as_view(), name='visualizar-sorteio'),
    url(r'^(?P<pk>\d+)/deletar/$', views.DeletarSorteio.as_view(), name='deletar-sorteio'),
    url(r'^novo/$', views.NovoSorteio.as_view(), name='novo-sorteio'),
    url(r'^criados/$', views.SorteiosCriados.as_view(), name='sorteios-criados'),
    url(r'^participando/$', views.SorteiosParticipando.as_view(), name='sorteios-participando'),
]