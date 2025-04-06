from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import autor

from .views import ClienteViewSet, autor

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('exportar/csv/', views.exportar_csv, name='exportar_csv'),
    path('exportar/pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('exportar/excel/', views.exportar_excel, name='exportar_excel'),
    path('', include(router.urls)),
    path('autor/', autor, name='autor'),

]