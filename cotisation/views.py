from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from Adherent.models import Adherent
from .models import Cotisation
from .forms import CotisationForm

# Liste des cotisations
def cotisation_list(request):
    cotisations = Cotisation.objects.all().order_by('-date_paiement')
    return render(request, 'cotisation/cotisation_list.html', {'cotisations': cotisations})

# Créer une nouvelle cotisation
def cotisation_create(request):
    adherent=Adherent.objects.all().order_by('last_name')
    if request.method == 'POST':
        form = CotisationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cotisation:cotisation')
    else:
        form = CotisationForm()
    return render(request, 'cotisation/cotisation_form.html', {'form': form, 'adherent':adherent})

# Détails d'une cotisation
def cotisation_detail(request, id):
    cotisation = get_object_or_404(Cotisation, id=id)
    return render(request, 'cotisation/cotisation_detail.html', {'cotisation': cotisation})

# Modifier une cotisation
def cotisation_modifier(request, id):
    adherent=Adherent.objects.all().order_by('last_name')
    cotisation = get_object_or_404(Cotisation, id=id)
    if request.method == 'POST':
        form = CotisationForm(request.POST, instance=cotisation)
        if form.is_valid():
            form.save()
            return redirect('cotisation:cotisation')
    else:
        form = CotisationForm(instance=cotisation)
    return render(request, 'cotisation/modifier_cotisation.html', {'form': form, 'adherent':adherent})

# Supprimer une cotisation
def cotisation_supprimer(request, id):
    cotisation = get_object_or_404(Cotisation, id=id)
    cotisation.delete()
    return redirect('cotisation:cotisation')
