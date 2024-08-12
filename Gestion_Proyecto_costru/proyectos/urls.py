from django.urls import path
from . import views

app_name = "projects"
urlpatterns = [
  path('', views.inicio, name="inicio"), 
  path('crearproyecto/', views.crearproyecto.as_view(), name="crearproyecto"),
  path('listarproyecto/', views.ListarProyecto.as_view(), name="mostrarproyecto"),
  
  path('editarproyecto/<int:pk>', views.actulizarproyecto.as_view(), name="editarproyecto"),
  path('eliminarproyecto/<int:pk>', views.eliminarproyecto.as_view(), name="eliminarproyecto"),

]