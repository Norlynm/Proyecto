from django.urls import path
from . import views

app_name = 'recursos'

urlpatterns = [
    path('', views.Recurso, name='recursos'),
    path('asignar/', views.asignar_recurso, name='asignar_recurso'),
]
