from django.db import models
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.
class Produkt(models.Model):
    nazwa = models.CharField(unique=True, max_length=30)
    opis = models.TextField(max_length=500)
    czy_dostepny = models.BooleanField(default=True)
    cena = models.PositiveIntegerField(validators=[MaxValueValidator(9999999)])

    class Meta:
        ordering = ['nazwa']

    def __str__(self):
        return self.nazwa

class Opinia(models.Model):
    komentarz = models.TextField(default='', max_length=500)
    STAR = {
        (1, '1/5 Zbyt Kiepski produkt'),
        (2, '2/5 Slaby produkt'),
        (3, '3/5 Średni produkt'),
        (4, '4/5 Dobry produkt'),
        (5, '5/5 Bardzo Dobry Produkt')
    }
    gwiazdki = models.IntegerField(choices=STAR, default=5)
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE, related_name='opinie')
    data_dodania = models.DateTimeField(auto_now_add=True)
    #autor = models.CharField(default='', max_length=30)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['data_dodania']

    def __str__(self):
        return str(self.produkt) + ', autor: ' + str(self.autor)

class Sklep(models.Model):
    nazwa_sklepu = models.CharField(max_length=30)
    adres_sklepu = models.URLField(null=True, blank=True)
    produkty = models.ManyToManyField(Produkt, related_name='produkty', blank=True)
    nip = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)], null=True, blank=True)
    telefon = PhoneNumberField(null=True, blank=True, unique=False)
    fax = PhoneNumberField(null=True, blank=True, unique=False)

    def __str__(self):
        return self.nazwa_sklepu


