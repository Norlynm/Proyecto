from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('', views.listar_archivos, name='listar_archivos'),
    path('subir/', views.subir_archivo, name='subir_archivo'),
]
