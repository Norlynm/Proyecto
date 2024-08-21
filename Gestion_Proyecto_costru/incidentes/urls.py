from django.urls import path
from . import views

app_name = 'incidentes'

urlpatterns = [
    path('', views.listar_incidentes, name='listar_incidentes'),
    path('reportar/', views.reportar_incidente, name='reportar_incidente'),
    path('resolver/<int:pk>/', views.resolver_incidente, name='resolver_incidente'),
]
