from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from . import views
from .models import Produkt, Sklep, Opinia
from rest_framework import status
from django.utils.http import urlencode
from django import urls
from django.contrib.auth.models import User

# Create your tests here.
class ProduktTests(APITestCase):
    def create_produkt(self, nazwa, opis, czy_dostepny, cena, client):
        url = reverse(views.ProduktList.view_name)
        data = {'nazwa': nazwa,
                'opis': opis,
                'czy_dostepny': czy_dostepny,
                'cena': cena}
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_produkt(self):
        user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')
        new_nazwa = 'Komputer stacjonarny'
        new_opis = 'Jest to komputer do gier'
        new_czy_dostepny = True
        new_cena = 3000
        response = self.create_produkt(new_nazwa, new_opis, new_czy_dostepny, new_cena, client)
        assert response.status_code == status.HTTP_201_CREATED
        assert Produkt.objects.count() == 1
        assert Produkt.objects.get().nazwa == new_nazwa
        assert Produkt.objects.get().opis == new_opis