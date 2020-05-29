from django.db import models
from datetime import datetime

# Create your models here.
class Carsforsale(models.Model):
    title = models.CharField(max_length= 200)
    time_and_date = models.DateTimeField(default= datetime.now, blank=True)
    car_picture = models.ImageField(upload_to='cars_pictures', blank=True)
    make_and_model = models.CharField(max_length= 200)
    car_description = models.TextField()
    contacts = models.TextField()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Carsforsale"