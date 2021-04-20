from rest_framework.relations import PrimaryKeyRelatedField

from .models import Produkt, Opinia, Sklep
from rest_framework import serializers

class ProduktSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = ['id', 'url', 'nazwa', 'opis', 'czy_dostepny', 'cena']

    def validate_cena(self, value):
        if value <= 0:
            raise serializers.ValidationError("Cena za produkt nie moze byc nizsza od zera", )
        return value

class OpiniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinia
        fields = ['id', 'url', 'komentarz', 'gwiazdki', 'produkt', 'data_dodania', 'autor']

    def validate_gwiazdki(self, value):
        if value <= 0 or value > 5:
            raise serializers.ValidationError("Nie mozesz dac mniej jak 1 gwiazdke i wiecej jak 5!", )
        return value

class SklepSerializer(serializers.ModelSerializer):
    produkty = ProduktSerializer(many=True, queryset=Produkt.objects.all())
    class Meta:
        model = Sklep
        fields = ['id', 'nazwa_sklepu', 'adres_sklepu', 'produkty', 'nip', 'telefon', 'fax']

