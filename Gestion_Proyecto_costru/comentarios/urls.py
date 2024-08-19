from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('<int:tarea_id>/', views.listar_comentarios, name='listar_comentarios'),
    path('agregar/<int:tarea_id>/', views.agregar_comentario, name='agregar_comentario'),
]
