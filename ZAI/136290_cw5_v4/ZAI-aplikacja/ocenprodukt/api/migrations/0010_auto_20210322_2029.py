# Generated by Django 3.1.7 on 2021-03-22 19:29

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210322_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='sklep',
            name='produkty',
            field=models.ManyToManyField(blank=True, related_name='produkty', to='api.Produkt'),
        ),
        migrations.AlterField(
            model_name='opinia',
            name='gwiazdki',
            field=models.IntegerField(choices=[(4, '4/5 Dobry produkt'), (5, '5/5 Bardzo Dobry Produkt'), (2, '2/5 Slaby produkt'), (1, '1/5 Zbyt Kiepski produkt'), (3, '3/5 Średni produkt')], default=5),
        ),
        migrations.AlterField(
            model_name='sklep',
            name='fax',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='sklep',
            name='nip',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='sklep',
            name='telefon',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
