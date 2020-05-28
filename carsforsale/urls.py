from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.cars),
    # url(r'carInfo', views.carInfo)
]