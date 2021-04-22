# Generated by Django 3.1.7 on 2021-03-22 19:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210322_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinia',
            name='gwiazdki',
            field=models.IntegerField(choices=[(1, '1/5 Zbyt Kiepski produkt'), (5, '5/5 Bardzo Dobry Produkt'), (2, '2/5 Slaby produkt'), (4, '4/5 Dobry produkt'), (3, '3/5 Średni produkt')], default=5),
        ),
        migrations.AlterField(
            model_name='sklep',
            name='fax',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sklep',
            name='nip',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='sklep',
            name='telefon',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
