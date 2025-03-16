from django.urls import path
from . import views

app_name = 'Adherent'

urlpatterns = [
    path('', views.adherent_list, name='Adherent'),
    path('creer/', views.adherent_create, name='creer'),
    path('<int:id>/', views.adherent_detail, name='infomation'),
    path('<int:id>/modifier/', views.modifier_adherent, name='modifier'),
    path('<int:id>/supprimer/', views.supprimer_adherent, name='supprimer'), 
 
]
