from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.listar_reportes, name='listar_reportes'),
    path('generar/', views.generar_reporte, name='generar_reporte'),
]
