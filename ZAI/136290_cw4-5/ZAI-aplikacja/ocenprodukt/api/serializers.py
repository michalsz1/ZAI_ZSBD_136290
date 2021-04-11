from .models import Produkt, Opinia
from rest_framework import serializers

class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = ['id', 'url', 'nazwa', 'opis', 'czy_dostepny']

class OpiniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinia
        fields = ['id', 'url', 'komentarz', 'gwiazdki', 'produkt', 'data_dodania', 'autor']