from django.shortcuts import render

# Create your views here.
from Appcoder.models import Familiares

def  mostrar_familiares(request):
    f1 = Familiares(nombre="Carlos Roman", edad=44, cumpleaños="1978-11-13")
    f2 = Familiares(nombre="Martin Roman", edad=23, cumpleaños="1999-01-07")
    f3 = Familiares(nombre="Maria Roman", edad=22, cumpleaños="2000-08-25" )
    return render(request, "familia.html", {"familia":[f1, f2, f3]})
