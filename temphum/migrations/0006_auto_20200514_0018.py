# Generated by Django 3.0.4 on 2020-05-14 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temphum', '0005_auto_20200514_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temphum',
            name='type',
            field=models.CharField(max_length=20, verbose_name='Tipo'),
        ),
    ]