from django.shortcuts import render, HttpResponse

# Create your views here.
def cars(request):
    return render(request, "carsforsale/cars.html")
    