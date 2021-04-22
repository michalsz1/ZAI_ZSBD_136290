# Generated by Django 3.1.7 on 2021-03-22 17:51

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinia',
            name='gwiazdki',
            field=models.IntegerField(choices=[(5, '5/5 Bardzo Dobry Produkt'), (1, '1/5 Zbyt Kiepski produkt'), (2, '2/5 Slaby produkt'), (4, '4/5 Dobry produkt'), (3, '3/5 Średni produkt')], default=5),
        ),
        migrations.AlterField(
            model_name='sklep',
            name='fax',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='sklep',
            name='produkty',
            field=models.ManyToManyField(blank=True, related_name='produkty', to='api.Produkt'),
        ),
        migrations.AlterField(
            model_name='sklep',
            name='telefon',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
