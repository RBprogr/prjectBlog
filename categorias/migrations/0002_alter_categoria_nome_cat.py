# Generated by Django 4.1.1 on 2022-09-18 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome_cat',
            field=models.CharField(max_length=255, verbose_name='Categoria'),
        ),
    ]