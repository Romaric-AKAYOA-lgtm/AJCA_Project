from django.urls import path
from . import views

app_name = 'prisecharge'

urlpatterns = [
    path('', views.prise_charge_list, name='liste'),
    path('creer/', views.prise_charge_create, name='creer'),
    path('<int:id>/', views.prise_charge_detail, name='information'),
    path('<int:id>/modifier/', views.prise_charge_modifier, name='modifier'),
    path('<int:id>/supprimer/', views.prise_charge_supprimer, name='supprimer'),
]
