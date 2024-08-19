from django.shortcuts import render, redirect
from .models import Archivo
from .forms import ArchivoForm  # Asegúrate de tener un formulario para la carga de archivos
from django.contrib.auth.decorators import login_required

@login_required  # Solo usuarios autenticados pueden ver los archivos
def listar_archivos(request):
    archivos = Archivo.objects.all()  # Podrías filtrar por proyecto o usuario si es necesario
    return render(request, 'files/listar_archivos.html', {'archivos': archivos})

@login_required  # Solo usuarios autenticados pueden subir archivos
def subir_archivo(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.save(commit=False)
            archivo.usuario = request.user  # Puedes asociar el archivo al usuario
            archivo.save()
            return redirect('files:listar_archivos')
    else:
        form = ArchivoForm()
    
    return render(request, 'files/subir_archivo.html', {'form': form})
