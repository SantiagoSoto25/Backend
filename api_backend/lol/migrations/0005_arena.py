# Generated by Django 4.1 on 2024-06-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0004_alter_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('modo', models.CharField(max_length=100)),
            ],
        ),
    ]
