# Generated by Django 4.1 on 2024-06-19 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0005_arena'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='arenas',
            field=models.ManyToManyField(blank=True, to='lol.arena'),
        ),
    ]
