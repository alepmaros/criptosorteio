from django.contrib import admin

# Register your models here.
from sorteios.models import Sorteio, Participacao, Comentario


@admin.register(Sorteio)
class SorteioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'hora_sorteio', 'privacidade', 'sorteado')

@admin.register(Participacao)
class SorteioAdmin(admin.ModelAdmin):
    list_display = ('user', 'sorteio', 'date_joined')

@admin.register(Comentario)
class SorteioAdmin(admin.ModelAdmin):
    list_display = ('display_nome_sorteio', 'display_nome', 'comentario')