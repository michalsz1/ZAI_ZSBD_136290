# Generated by Django 3.1.7 on 2021-03-16 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('opis', models.TextField(max_length=500)),
                ('czy_dostepny', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sklep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_sklepu', models.CharField(max_length=30)),
                ('adres_sklepu', models.URLField()),
                ('produkty', models.ManyToManyField(to='api.Produkt')),
            ],
        ),
        migrations.CreateModel(
            name='Opinia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('komentarz', models.TextField(default='', max_length=500)),
                ('gwiazdki', models.IntegerField(default=5)),
                ('data_dodania', models.DateTimeField()),
                ('produkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinie', to='api.produkt')),
            ],
        ),
    ]
