# Generated by Django 3.0.6 on 2020-05-29 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carsforsale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('time_and_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('car_picture', models.ImageField(blank=True, upload_to='cars_pictures')),
                ('make_and_model', models.CharField(max_length=200)),
                ('car_description', models.TextField()),
                ('contacts', models.TextField()),
            ],
        ),
    ]