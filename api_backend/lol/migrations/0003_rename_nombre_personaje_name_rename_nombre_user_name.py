# Generated by Django 4.1 on 2024-06-19 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0002_personaje_movimiento_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personaje',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nombre',
            new_name='name',
        ),
    ]
