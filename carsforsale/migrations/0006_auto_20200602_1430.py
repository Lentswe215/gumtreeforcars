# Generated by Django 3.0.6 on 2020-06-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsforsale', '0005_auto_20200602_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsforsale',
            name='mileage',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
