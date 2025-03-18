from django.urls import path
from . import views

app_name = 'medecin'

urlpatterns = [
    path('', views.medecin_list, name='medecin'),
    path('creer/', views.medecin_create, name='creer'),
    path('<int:id>/', views.medecin_detail, name='information'),
    path('<int:id>/modifier/', views.modifier_medecin, name='modifier'),
    path('<int:id>/supprimer/', views.supprimer_medecin, name='supprimer'), 
]
