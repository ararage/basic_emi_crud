# Generated by Django 3.1 on 2020-08-14 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date/Time when the record has been created')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Last Date/Time when the record has been updated')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del arma.')),
                ('places', models.IntegerField(default=0, verbose_name='Número de lugares disponibles.')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
