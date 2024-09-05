from django.shortcuts import render
from .models import Reporte
from.form import ReporteForm
from django.shortcuts import redirect

def crear_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ReporteForm()
    return render(request, 'reporte/listar_reportes.html', {'form': form})
    

def generar_reporte(request):
    return render(request,'reporte/listar_reportes.html')
    


def listar_reportes(request):
    reportes = Reporte.objects.all()  # Obtener todos los reportes
    return render(request, 'listar_reportes.html', {'reportes': reportes})
