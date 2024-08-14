from django.urls import path
from . import views

app_name = 'tareas'

urlpatterns = [
    path('creartarea/', views.CrearTarea.as_view(), name='creartarea'),
    path('listartareas/', views.ListarTareas.as_view(), name='listartareas'),
    path('editartarea/<int:pk>/', views.ActualizarTarea.as_view(), name='editartarea'),
    path('detalletarea/<int:pk>/', views.DetalleTarea.as_view(), name='detalletarea'),
]
