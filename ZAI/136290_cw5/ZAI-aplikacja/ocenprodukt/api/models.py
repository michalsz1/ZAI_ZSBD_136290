from django.db import models

# Create your models here.
class Produkt(models.Model):
    nazwa = models.CharField(max_length=30)
    opis = models.TextField(max_length=500)
    czy_dostepny = models.BooleanField(default=True)

    class Meta:
        ordering = ['nazwa']

    def __str__(self):
        return self.nazwa

class Opinia(models.Model):
    komentarz = models.TextField(default='', max_length=500)
    gwiazdki = models.IntegerField(default=5)
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE, related_name='opinie')
    data_dodania = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(default='', max_length=30)

    class Meta:
        ordering = ['data_dodania']

class Sklep(models.Model):
    nazwa_sklepu = models.CharField(max_length=30)
    adres_sklepu = models.URLField()
    produkty = models.ManyToManyField(Produkt)
