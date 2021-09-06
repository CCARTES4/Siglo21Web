
from django.urls import path
from .views import home,carta,reservar,nosotros,consReserva



urlpatterns = [
    path('', home, name="home"),
    path('carta/',carta, name="carta"),
    path('reservar/',reservar, name="reservar"),
    path('nosotros/',nosotros, name="nosotros"),
    path('consReserva/',consReserva, name="consReserva")
]