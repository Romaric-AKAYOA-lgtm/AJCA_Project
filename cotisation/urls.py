from django.urls import path
from . import views

app_name = 'cotisation'

urlpatterns = [
    path('', views.cotisation_list, name='cotisation'),  # Liste des cotisations
    path('creer/', views.cotisation_create, name='cotisation_create'),  # Création d'une cotisation
    path('<int:id>/', views.cotisation_detail, name='cotisation_detail'),  # Détails d'une cotisation
    path('<int:id>/modifier/', views.cotisation_modifier, name='cotisation_modifier'),  # Modification d'une cotisation
    path('<int:id>/supprimer/', views.cotisation_supprimer, name='cotisation_supprimer'),  # Suppression d'une cotisation
]
