from django.urls import path
from . import views

app_name = 'Tuteur'

urlpatterns = [
    path('', views.tuteur_list, name='Tuteur'),
    path('creer/', views.tuteur_create, name='creer'),
    path('<int:id>/', views.tuteur_detail, name='infomation'),
    path('<int:id>/modifier/', views.modifier_tuteur, name='modifier'),
    path('<int:id>/supprimer/', views.supprimer_tuteur, name='supprimer'), 
 
]
