from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def vistaUno(request):
    return HttpResponse("<h1 style='color:red'>Hola mundo App1 </h1>")
