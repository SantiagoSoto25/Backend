from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0006_user_arenas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('coste', models.IntegerField()),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='skins',
            field=models.ManyToManyField(blank=True, to='lol.skin'),
        ),
    ]
