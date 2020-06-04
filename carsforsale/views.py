from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Carsforsale


# Create your views here.
def cars(request):
    carsAvailable = Carsforsale.objects.order_by('date')[:20]

    return render(request, "carsforsale/cars.html",{
        "cars" : carsAvailable
    })

def carInfo(request, id):

    currentCar = Carsforsale.objects.get(id=id)
    return render(request, "carsforsale/car_info.html",{
        "car": currentCar
    })
    
def example(request):
    visitorinfo = Visitor.objects.all()
    return render(request, "carsforsale/admin_page.html", {
        "visitors" : visitorinfo
    })

def success(request):
    fullname = request.POST["fullname"]
    age = request.POST["age"]
    date_of_visit = request.POST["date_of_visit"]
    time_of_visit = request.POST["time_of_visit"]
    assisted_by = request.POST["assisted_by"]
    comments = request.POST["comments"]

    visitor = Visitor(fullname= fullname, age=age, date_of_visit=date_of_visit, time_of_visit=time_of_visit, assisted_by=assisted_by, comments=comments)
    visitor.save()

    return HttpResponseRedirect('/example')
    
    