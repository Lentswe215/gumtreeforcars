# Generated by Django 3.0.6 on 2020-06-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsforsale', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carsforsale',
            options={'verbose_name_plural': 'Carsforsale'},
        ),
        migrations.RemoveField(
            model_name='carsforsale',
            name='contacts',
        ),
        migrations.AddField(
            model_name='carsforsale',
            name='color',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='carsforsale',
            name='email',
            field=models.EmailField(default='example@gmail.com', max_length=200),
        ),
        migrations.AddField(
            model_name='carsforsale',
            name='fuel_type',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='carsforsale',
            name='manufactured',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddField(
            model_name='carsforsale',
            name='phone',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='carsforsale',
            name='price',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='carsforsale',
            name='transmission',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='carsforsale',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]