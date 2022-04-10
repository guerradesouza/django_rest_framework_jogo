from django.contrib import admin

# Register your models here.

from .models import Jogo

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('liga', 'nomeTime1', 'nomeTime2', 'dataDoJogo', 'hora')
