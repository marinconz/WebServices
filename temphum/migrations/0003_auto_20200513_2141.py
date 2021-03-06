# Generated by Django 3.0.4 on 2020-05-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temphum', '0002_auto_20200513_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='temphum',
            name='latitud',
            field=models.CharField(default=0, max_length=50, verbose_name='Latitud'),
        ),
        migrations.AddField(
            model_name='temphum',
            name='longitud',
            field=models.CharField(default=0, max_length=20, verbose_name='Longitud'),
        ),
        migrations.AddField(
            model_name='temphum',
            name='tipo_Terreno',
            field=models.CharField(default=0, max_length=20, verbose_name='TipoTerreno'),
        ),
        migrations.AlterField(
            model_name='temphum',
            name='type',
            field=models.CharField(max_length=20, verbose_name='Tipo'),
        ),
    ]
