# Generated by Django 5.0.3 on 2024-03-30 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_publications_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publications',
            options={'verbose_name_plural': 'Publications'},
        ),
    ]
