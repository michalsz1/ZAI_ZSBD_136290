# Generated by Django 3.1.7 on 2021-03-23 15:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30, unique=True)),
                ('opis', models.TextField(max_length=500)),
                ('czy_dostepny', models.BooleanField(default=True)),
                ('cena', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999)])),
            ],
            options={
                'ordering': ['nazwa'],
            },
        ),
        migrations.CreateModel(
            name='Sklep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_sklepu', models.CharField(max_length=30)),
                ('adres_sklepu', models.URLField(blank=True, null=True)),
                ('nip', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('telefon', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('fax', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('produkty', models.ManyToManyField(blank=True, related_name='produkty', to='api.Produkt')),
            ],
        ),
        migrations.CreateModel(
            name='Opinia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('komentarz', models.TextField(default='', max_length=500)),
                ('gwiazdki', models.IntegerField(choices=[(1, '1/5 Zbyt Kiepski produkt'), (5, '5/5 Bardzo Dobry Produkt'), (4, '4/5 Dobry produkt'), (2, '2/5 Slaby produkt'), (3, '3/5 Średni produkt')], default=5)),
                ('data_dodania', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('produkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinie', to='api.produkt')),
            ],
            options={
                'ordering': ['data_dodania'],
            },
        ),
    ]