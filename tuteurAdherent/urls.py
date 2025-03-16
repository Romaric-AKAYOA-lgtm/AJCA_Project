from django.urls import path
from . import views

app_name = 'tuteurAdherent'

urlpatterns = [
    path('', views.tuteurAdherent_list, name='Adherent'),
    path('creer/', views.tuteurAdherent_create, name='creer'),
    path('<int:id>/', views.tuteurAdherentt_detail, name='infomation'),
    path('<int:id>/modifier/', views.modifier_tuteurAdherent, name='modifier'),
    path('<int:id>/supprimer/', views. supprimer_tuteurAdherent, name='supprimer'), 
]
