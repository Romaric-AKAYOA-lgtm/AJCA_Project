from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from Activation.models import Activation
from .models import Fonction
from .forms import  FonctionForm
 
def fonction_list(request):
    """Affiche la page d'accueil avec la gestion du personnel et la vérification d'activation."""
    
    # 🔹 Vérifier l'activation
    activation = Activation.objects.first()
    if not activation or not activation.is_valid():
        return redirect("Activation:activation_page")  # Redirige vers une page d'activation si expiré

    fonction = Fonction.objects.all().order_by('designation')
    return render(request, 'fonction/fonction_list.html', {
       'fonction': fonction})

def fonction_create(request):
    if request.method == "POST":
        form = FonctionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fonction:fonction')
    else:
        form = FonctionForm()
    return render(request, 'fonction/fonction_form.html', {'form': form})

def fonction_detail(request, id):
    fonction= get_object_or_404(Fonction, id=id)
    return render(request, 'fonction/fonction_detail.html', {'directeur': fonction})

def modifier_fonction(request, id):
    fonction = get_object_or_404(Fonction, id=id)

    if request.method == "POST":
        form =FonctionForm(request.POST, instance=fonction)
        if form.is_valid():
            form.save()
            return redirect('fonction:fonction')  # Redirigez vers la liste des fonction après la sauvegarde
    else:
        form =FonctionForm (instance=fonction)  # Remplir le formulaire avec les données existantes

    return render(request, 'fonction/fonction_form_edit.html', {'form': form, 'fonction': fonction})

def supprimer_fonction(request, id):
    fonction = get_object_or_404(Fonction , id=id)
    fonction.delete()
    return redirect('fonction:fonction')
