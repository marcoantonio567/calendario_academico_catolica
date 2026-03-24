from django.contrib import admin
from .models import Evento


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_inicio', 'data_fim')
    list_filter = ('categoria',)
    search_fields = ('titulo',)
    ordering = ('data_inicio',)
