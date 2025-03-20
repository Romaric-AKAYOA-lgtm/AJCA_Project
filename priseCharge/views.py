from django.shortcuts import render, get_object_or_404, redirect
from .models import PriseCharge
from .forms import PriseChargeForm

def prise_charge_list(request):
    """Affiche la liste de toutes les prises en charge."""
    prises_charges = PriseCharge.objects.all()
    return render(request, 'prisecharge/liste.html', {'prises_charges': prises_charges})

def prise_charge_create(request):
    """Permet de créer une nouvelle prise en charge."""
    if request.method == "POST":
        form = PriseChargeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prisecharge:liste')
    else:
        form = PriseChargeForm()
    return render(request, 'prisecharge/creer.html', {'form': form})

def prise_charge_detail(request, id):
    """Affiche les détails d'une prise en charge spécifique."""
    prise_charge = get_object_or_404(PriseCharge, id=id)
    return render(request, 'prisecharge/detail.html', {'prise_charge': prise_charge})

def prise_charge_modifier(request, id):
    """Permet de modifier une prise en charge existante."""
    prise_charge = get_object_or_404(PriseCharge, id=id)
    if request.method == "POST":
        form = PriseChargeForm(request.POST, instance=prise_charge)
        if form.is_valid():
            form.save()
            return redirect('prisecharge:liste')
    else:
        form = PriseChargeForm(instance=prise_charge)
    return render(request, 'prisecharge/modifier.html', {'form': form, 'prise_charge': prise_charge})

def prise_charge_supprimer(request, id):
    """Permet de supprimer une prise en charge."""
    prise_charge = get_object_or_404(PriseCharge, id=id)
    if request.method == "POST":
        prise_charge.delete()
        return redirect('prisecharge:liste')
    return render(request, 'prisecharge/supprimer.html', {'prise_charge': prise_charge})
