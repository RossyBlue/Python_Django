# Generated by Django 4.0.5 on 2023-07-23 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_alter_vehiculomodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculomodel',
            options={'permissions': (('visualizar_catalogo', 'Puede visualizar_catalogo'),), 'verbose_name_plural': 'Usuario registrado'},
        ),
    ]
