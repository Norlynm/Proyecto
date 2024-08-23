from django.urls import path
from . import views

app_name = 'calendar'

urlpatterns = [
    path('', views.listar_eventos, name='listar_eventos'),
    path('agregar/', views.agregar_evento, name='agregar_evento'),
]
