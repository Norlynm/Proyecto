from django.urls import path
from . import views

app_name = 'tareas'

urlpatterns = [

    path('', views.tarea, name='tareaInicio'),
    path('creartarea/', views.CrearTarea.as_view(), name='creartarea'),
    path('listartareas/', views.ListarTareas.as_view(), name='listartareas'),
    path('editartarea/<int:pk>', views.ActualizarTarea.as_view(), name='editartarea'),
    path('tareas_detalle/<int:pk>/', views.DetalleTarea.as_view(), name='tareas_detalle'),
   
]
