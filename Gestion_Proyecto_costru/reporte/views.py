from django.shortcuts import render
from .models import Reporte
from.form import ReporteForm


def listar_reportes(request):
    if  request.method =="GET":
        return render(request,'reporte/listar_reportes.html',{
            'form': ReporteForm
        })
    else:
        reportes = Reporte.objects.all()
        reportes.save() #Aqui me vas a guardar el archivo que mandaron junto a una descripcion
        return render(request, 'reporte/listar_reportes.html', {'reportes': reportes})

def generar_reporte(request):
   from django.db import models

