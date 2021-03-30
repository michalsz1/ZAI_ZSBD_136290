from .models import Produkt, Opinia
from rest_framework import serializers

class ProduktSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produkt
        fields = ['id', 'nazwa', 'opis', 'czy_dostepny']


class OpiniaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opinia
        fields = ['id', 'komentarz', 'gwiazdki', 'produkt', 'data_dodania', 'autor']
