# Generated by Django 3.0.6 on 2020-06-12 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carsforsale', '0012_auto_20200604_1738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carsforsale',
            options={'verbose_name_plural': 'Carsforsale'},
        ),
        migrations.AlterUniqueTogether(
            name='carsforsale',
            unique_together=set(),
        ),
    ]
