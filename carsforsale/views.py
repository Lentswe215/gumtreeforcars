from django.shortcuts import render
from .models import Carsforsale

# Create your views here.
def cars(request):
    carsAvailable = Carsforsale.objects.all()

    return render(request, "carsforsale/cars.html",{
        "cars" : carsAvailable
    })

def carInfo(request, id):

    currentCar = Carsforsale.objects.get(id=id)
    return render(request, "carsforsale/car_info.html",{
        "car": currentCar
    })
    