from django.urls import path
from . import views

app_name = "proyectos"
urlpatterns = [
  path('proyecto/', views.inicio, name="inicio"), 
  path('crearproyecto/', views.crearproyecto.as_view(), name="crearproyecto"),
  path('listarproyecto/', views.ListarProyecto.as_view(), name="mostrarproyecto"),

  path('editarproyecto/<int:pk>', views.actulizarproyecto.as_view(), name="editarproyecto"),
  path('eliminarproyecto/<int:pk>', views.eliminarproyecto.as_view(), name="eliminarproyecto"),
  path('crearequipo/', views.crearequipo.as_view(), name='crearequipo'),
  path('eliminarequipo/<int:pk>',views.eliminarequipo.as_view(), name='eliminarequipo'),
  path('mostrarequipo/', views.ListarEquipos.as_view(), name="mostrarequipo"),
  path('editarequipo/<int:pk>/', views.editarequipo.as_view(), name='editarequipo'),
  
  
  
]