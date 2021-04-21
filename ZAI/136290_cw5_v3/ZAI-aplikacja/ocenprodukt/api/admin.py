from django.contrib import admin
from .models import Produkt, Opinia, Sklep
from django.utils.html import format_html
# Register your models here.
#admin.site.register(Produkt)
#admin.site.register(Opinia)
#admin.site.register(Sklep)

class OpiniaPodProduktami(admin.TabularInline):
    model = Opinia


@admin.register(Produkt)
class ProduktAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'cena']
    search_fields = ['produkt']
    inlines = [
        OpiniaPodProduktami
    ]

@admin.register(Opinia)
class OpiniaAdmin(admin.ModelAdmin):
    list_display = ['produkt', 'gwiazdki', 'autor']
    list_filter = ['gwiazdki']


@admin.register(Sklep)
class SklepAdmin(admin.ModelAdmin):
    list_display = ['nazwa_sklepu', 'pokaz_adres_sklepu', 'telefon']
    def pokaz_adres_sklepu(self, obj):
        if obj.adres_sklepu is not None:
            return format_html(f'<a href="{obj.adres_sklepu}" target="_blank">{obj.adres_sklepu}</a>')
        else:
            return ''

    pokaz_adres_sklepu.short_description = 'Adres Sklepu'
