from django.contrib import admin

from django.contrib import admin
from .models import Aldeia


@admin.register(Aldeia)
class AldeiaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'municipio',
        'etnia',
        'populacao',
    )

    search_fields = (
        'nome',
        'municipio',
        'etnia',
    )
