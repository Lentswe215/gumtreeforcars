from django.db import models
from datetime import datetime


# Create your models here.
class Carsforsale(models.Model):
    title = models.CharField(default="", max_length= 200)
    time_and_date = models.DateTimeField(default= datetime.now, blank=True)
    car_picture = models.ImageField(upload_to='cars_pictures', blank=True)
    price = models.CharField(default=0, max_length= 10) 
    make_and_model = models.CharField(max_length= 200)
    manufactured = models.CharField(max_length=4, default="")
    mileage = models.IntegerField(default=0)
    transmission = models.CharField(default="", max_length=200)
    fuel_type = models.CharField(default="", max_length= 10)
    color =  models.CharField(default="", max_length= 200)
    car_description = models.TextField()
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    phone = models.CharField(max_length=10, default=0)
    email = models.EmailField(default="example@gmail.com", max_length= 200)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Carsforsale"