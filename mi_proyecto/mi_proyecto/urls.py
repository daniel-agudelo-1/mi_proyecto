from django.contrib import admin
from django.urls import path, include
from gestion.views import autor


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion.urls')),
    path('autor/', autor, name='autor'),

]