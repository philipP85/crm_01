# Generated by Django 4.2.17 on 2025-02-26 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auftraege', '0009_remove_auftrag_summe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auftragleistung',
            name='summe',
        ),
    ]
