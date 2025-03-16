from django.shortcuts import render, redirect
from datetime import date, timedelta
from Activation.models import Activation

def  home_view(request):
    """Page d'accueil avec les listes des directeurs, secrétaires, visiteurs et visites"""
    
    # Vérification de la validité de la clé d'activation via activation_view
    # 🔹 Vérifier l'activation
    activation = Activation.objects.first()
    if not activation or not activation.is_valid():
        return redirect("Activation:activation_page")  # Redirige vers une page d'activation si expiré


    today = date.today()
    week_start = today - timedelta(days=today.weekday())  # Lundi de la semaine
    month_start = today.replace(day=1)  # Début du mois

    # Log de la transaction effectuée par l'utilisateur
    context = {


    }

    return render(request, "home.html", context)
