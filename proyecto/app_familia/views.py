from django.http import HttpResponse
from django.shortcuts import render
from app_familia.models import Familia
from django.template import loader
from django.template import Template, Context

# Create your views here.


def familia(request):
    familia = Familia.objects.all()
    dicc = {"familia": familia}
    plantilla = loader.get_template("template.html")
    documento = plantilla.render(dicc)


    return HttpResponse(documento)
