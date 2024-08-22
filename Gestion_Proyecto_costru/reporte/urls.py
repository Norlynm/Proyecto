from django.urls import path
from . import views

app_name = 'reporte'

urlpatterns = [
    path('listar/', views.listar_reportes, name='listar_reportes'),
    path('generar/', views.generar_reporte, name='generar_reporte'),
]