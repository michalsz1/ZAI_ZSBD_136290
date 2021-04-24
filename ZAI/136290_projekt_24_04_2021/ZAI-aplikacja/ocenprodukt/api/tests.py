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


    def test_post_existing_produkt(self):
        user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')

        new_nazwa = 'Komputer stacjonarny'
        new_opis = 'Jest to komputer do gier'
        new_czy_dostepny = True
        new_cena = 3000
        response_one = self.create_produkt(new_nazwa, new_opis, new_czy_dostepny, new_cena, client)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.create_produkt(new_nazwa, new_opis, new_czy_dostepny, new_cena, client)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST


    def test_update_produkt(self):
        user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')
        new_nazwa = 'Komputer stacjonarny'
        new_opis = 'Jest to komputer do gier'
        new_czy_dostepny = True
        new_cena = 3000
        response = self.create_produkt(new_nazwa, new_opis, new_czy_dostepny, new_cena, client)

        url = urls.reverse(views.ProduktDetail.view_name, None, {response.data['id']})
        updated_new_nazwa = 'New Komputer'
        data = {'nazwa': updated_new_nazwa}
        patch_response = client.patch(url, data, format='json')

        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['nazwa'] == updated_new_nazwa

class OpiniaTests(APITestCase):
    def create_produkt(self, nazwa, opis, czy_dostepny, cena, client):
        url = reverse(views.ProduktList.view_name)
        data = {'nazwa': nazwa,
                'opis': opis,
                'czy_dostepny': czy_dostepny,
                'cena': cena}
        response = client.post(url, data, format='json')
        return response

    def create_opinia(self, komentarz, gwiazdki, produkt, autor, client):
        url = reverse(views.OpiniaList.view_name)
        data = {'komentarz': komentarz,
                'gwiazdki': gwiazdki,
                'produkt': produkt,
                'autor': autor}
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_opinia(self):
        user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')
        # PRODUKT
        new_nazwa = 'Komputer stacjonarny'
        new_opis = 'Jest to komputer do gier'
        new_czy_dostepny = True
        new_cena = 3000
        response_one = self.create_produkt(new_nazwa, new_opis, new_czy_dostepny, new_cena, client)
        assert response_one.status_code == status.HTTP_201_CREATED
        assert Produkt.objects.count() == 1
        assert Produkt.objects.get().nazwa == new_nazwa
        assert Produkt.objects.get().opis == new_opis

        # OPINIA
        new_komentarz = 'Test Komentarza'
        new_gwiazdki = 3
        new_produkt = 'Komputer stacjonarny'
        new_autor = 'admin'
        response_two = self.create_opinia(new_komentarz, new_gwiazdki, new_produkt, new_autor, client)
        assert response_two.status_code == status.HTTP_201_CREATED
        assert Opinia.objects.count() == 1
        assert Opinia.objects.get().komentarz == new_komentarz
        assert Opinia.objects.get().gwiazdki == new_gwiazdki
        assert Opinia.objects.get().produkt.nazwa == new_produkt
