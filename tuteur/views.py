from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tuteur
from .forms import TuteurForm

def tuteur_list(request):
    # Afficher la liste des adhérents
    tuteur = Tuteur.objects.all().order_by("-date_creation")
    return render(request, 'Tuteur/tuteur_list.html', context={'tuteur': tuteur})

def tuteur_create(request):
    form = TuteurForm()
    if request.method == 'POST':
        form = TuteurForm(request.POST, request.FILES)
        if form.is_valid():  # Vérifier si le formulaire est valide
            form.save()
            return HttpResponseRedirect(reverse('Tuteur:Tuteur'))
        else:
            print(form.errors)  # Debug : Affiche les erreurs de validation dans la console

    return render(request, 'Tuteur/tuteur_create.html', context={'form': form})

def tuteur_detail(request, id):
    # Afficher les détails d'un adhérent spécifique
    tuteur = get_object_or_404(Tuteur, id=id)
    return render(request, 'Tuteur/tuteur_detail.html', {'tuteur': tuteur})

# Vue pour modifier un adhérent
def modifier_tuteur(request, id):
    tuteur = get_object_or_404(Tuteur, id=id)
    if request.method == 'POST':
        form = TuteurForm(request.POST, instance=tuteur)
        if form.is_valid():
            form.save()
            return redirect('Tuteur:Tuteur')  # Redirection vers la liste des adhérents
    else:
        form = TuteurForm(instance=tuteur)
    return render(request, 'Tuteur/modifier_tuteur.html', {'form': form, 'tuteur': tuteur})

# Vue pour supprimer un adhérent
def supprimer_tuteur(request, id):
    tuteur = get_object_or_404(Tuteur, id=id)
    if request.method == 'POST':
        tuteur.delete()
        return redirect('Tuteur:Tuteur')  # Redirection vers la liste des adhérents
    return render(request, 'Tuteur/supprimer_tuteur.html', {'tuteur': tuteur})