from django.urls import path
from . import views

app_name = 'reporte'

urlpatterns = [
    
     path('crear/', views.crear_reporte, name='crear_reporte'),
    path('detalles/<int:pk>/', views.detalle_reporte, name='detalle_reporte'),
    path('listar/', views.listar_reportes, name='listar_reportes'),
     path('inicio/',views.inicio, name='inicio')
    ]