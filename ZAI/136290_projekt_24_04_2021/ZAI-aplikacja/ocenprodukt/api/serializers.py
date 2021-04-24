from rest_framework.relations import PrimaryKeyRelatedField
from .models import Produkt, Opinia, Sklep
from rest_framework import serializers
from django.contrib.auth.models import User

class ProduktSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.HyperlinkedRelatedField(read_only=True, view_name='produkt-detail')

    class Meta:
        model = Produkt
        fields = ['id', 'nazwa', 'opis', 'czy_dostepny', 'cena']

    def validate_cena(self, value):
        if value <= 0:
            raise serializers.ValidationError("Cena za produkt nie moze byc nizsza od zera", )
        return value

class OpiniaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedRelatedField(read_only=True, view_name='opinia-detail')
    produkt = serializers.SlugRelatedField(queryset=Produkt.objects.all(), slug_field='nazwa')
    #produkt = serializers.HyperlinkedRelatedField(read_only=True, view_name='produkt-detail')
    autor = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Opinia
        fields = ['id', 'komentarz', 'gwiazdki', 'produkt', 'data_dodania', 'autor']

    def validate_gwiazdki(self, value):
        if value <= 0 or value > 5:
            raise serializers.ValidationError("Nie mozesz dac mniej jak 1 gwiazdke i wiecej jak 5!", )
        return value

class SklepSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedRelatedField(read_only=True, view_name='sklep-detail')
    produkty = serializers.HyperlinkedRelatedField(many=True, queryset=Produkt.objects.all(), view_name='produkt-detail')
    #produkty = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='produkt-detail')

    class Meta:
        model = Sklep
        fields = ['id', 'nazwa_sklepu', 'adres_sklepu', 'produkty', 'nip', 'telefon', 'fax']


