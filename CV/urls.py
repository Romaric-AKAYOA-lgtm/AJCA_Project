from django.urls import path
from . import views

app_name = 'CV'

urlpatterns = [
    path('', views.cv_list, name='cv_list'),
    path('ajouter/', views.cv_create, name='cv_create'),
    path('<int:id>/', views.cv_detail, name='cv_detail'),
    path('<int:id>/modifier/', views.cv_modifier, name='cv_modifier'),
]
