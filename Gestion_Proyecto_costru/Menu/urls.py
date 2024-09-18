
from django.urls import path
from Menu import views

app_name = "Menu"

urlpatterns = [
    path('',views.principal, name="principal"),
    path('Cerrar_Sesion/',views.cerrar_sesion, name='Cerrar_sesion'),
    path('inicio_sesion/',views.inicio_sesion,name="iniciar_sesion"),
    path('Usuario/',views.usuario,name="usuario"),
    path('registro/',views.registro, name="registro"),
    path('calendario/', views.calendario, name='calendario'),
    path('mostrar_calendario/', views.mostrar_calendario, name='mostrar_calendario'),
    path('despedida/', views.despedida, name='despedida'),
]