# Generated by Django 3.0.6 on 2020-06-02 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsforsale', '0006_auto_20200602_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsforsale',
            name='fuel_type',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Petrol', 'Petrol')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='carsforsale',
            name='transmission',
            field=models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], default='Select', max_length=20),
        ),
    ]
