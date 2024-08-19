from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.listar_notificaciones, name='listar_notificaciones'),
    path('leida/<int:pk>/', views.marcar_como_leida, name='marcar_como_leida'),
]
