from django.urls import path
from . import views

app_name = 'reporte'

urlpatterns = [
    path('listar/', views.generar_reporte, name='listar_reportes'),
    path('generar/', views.crear_reporte, name='generar_reporte'),
]