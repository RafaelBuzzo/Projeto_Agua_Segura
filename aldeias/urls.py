from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_aldeias, name='aldeias'),
    path('nova/', views.nova_aldeia, name='nova_aldeia'),
]