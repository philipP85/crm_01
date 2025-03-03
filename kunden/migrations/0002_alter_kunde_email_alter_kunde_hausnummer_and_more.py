# Generated by Django 4.2.17 on 2025-02-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kunden', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kunde',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='kunde',
            name='hausnummer',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='kunde',
            name='ort',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kunde',
            name='plz',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='kunde',
            name='strasse',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
