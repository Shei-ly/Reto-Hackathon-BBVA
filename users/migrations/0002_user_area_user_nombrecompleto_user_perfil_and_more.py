# Generated by Django 4.0.5 on 2022-07-14 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='area',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='nombreCompleto',
            field=models.CharField(default=True, max_length=150),
        ),
        migrations.AddField(
            model_name='user',
            name='perfil',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='segmento',
            field=models.SmallIntegerField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ubicacion',
            field=models.CharField(default=True, max_length=50),
        ),
    ]
