from django.contrib import admin

# Register your models here.
from sorteios.models import Sorteio, Comentario


@admin.register(Sorteio)
class SorteioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'hora_sorteio', 'privacidade', 'sorteado')

@admin.register(Comentario)
class SorteioAdmin(admin.ModelAdmin):
    list_display = ('display_nome_sorteio', 'display_nome', 'comentario')