from rest_framework.relations import PrimaryKeyRelatedField

from .models import Produkt, Opinia, Sklep
from rest_framework import serializers

class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = ['id', 'nazwa', 'opis', 'czy_dostepny', 'cena']

    def validate_cena(self, value):
        if value <= 0:
            raise serializers.ValidationError("Cena za produkt nie moze byc nizsza od zera", )
        return value

class OpiniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinia
        fields = ['id', 'komentarz', 'gwiazdki', 'produkt', 'data_dodania', 'autor']

    def validate_gwiazdki(self, value):
        if value <= 0 or value > 5:
            raise serializers.ValidationError("Nie mozesz dac mniej jak 1 gwiazdke i wiecej jak 5!", )
        return value

class SklepSerializer(serializers.ModelSerializer):
    #p#rodukty = ProduktSerializer(many=True, queryset=Produkt.objects.all())
    produkty = serializers.HyperlinkedRelatedField(many=True, queryset=Produkt.objects.all(), view_name='produkt-detail')
    class Meta:
        model = Sklep
        fields = ['id', 'nazwa_sklepu', 'adres_sklepu', 'produkty', 'nip', 'telefon', 'fax']