from django.shortcuts import render
from .models import Reporte

def listar_reportes(request):
    reportes = Reporte.objects.all()
    return render(request, 'reporte/listar_reportes.html', {'reportes': reportes})

def generar_reporte(request):
    # Lógica para generar el reporte (puede ser un PDF, Excel, etc.)
    # Aquí puedes usar librerías como `ReportLab` o `Pandas`
    pass
