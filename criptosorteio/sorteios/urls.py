from django.conf.urls import url

from sorteios.views import SorteiosView

urlpatterns = [
    url(r'^$', SorteiosView.as_view(), name='sorteios'),
]