# Generated by Django 3.1.7 on 2021-03-22 19:41

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20210322_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='testowa',
            name='fax',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='testowa',
            name='nip',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AddField(
            model_name='testowa',
            name='telefon',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='opinia',
            name='gwiazdki',
            field=models.IntegerField(choices=[(5, '5/5 Bardzo Dobry Produkt'), (3, '3/5 Średni produkt'), (2, '2/5 Slaby produkt'), (4, '4/5 Dobry produkt'), (1, '1/5 Zbyt Kiepski produkt')], default=5),
        ),
    ]
