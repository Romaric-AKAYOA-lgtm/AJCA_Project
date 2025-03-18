from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Medecin
from .forms import MedecinForm

def medecin_list(request):
    medecins = Medecin.objects.all().order_by("-date_creation")
    return render(request, 'Medecin/medecin_list.html', context={'medecins': medecins})

def medecin_create(request):
    form = MedecinForm()
    if request.method == 'POST':
        form = MedecinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('medecin:medecin'))
        else:
            print(form.errors)
    return render(request, 'Medecin/medecin_create.html', context={'form': form})

def medecin_detail(request, id):
    medecin = get_object_or_404(Medecin, id=id)
    return render(request, 'Medecin/medecin_detail.html', {'medecin': medecin})

def modifier_medecin(request, id):
    medecin = get_object_or_404(Medecin, id=id)
    if request.method == 'POST':
        form = MedecinForm(request.POST, instance=medecin)
        if form.is_valid():
            form.save()
            return redirect('medecin:medecin')
    else:
        form = MedecinForm(instance=medecin)
    return render(request, 'Medecin/modifier_medecin.html', {'form': form, 'medecin': medecin})

def supprimer_medecin(request, id):
    medecin = get_object_or_404(Medecin, id=id)
    if request.method == 'POST':
        medecin.delete()
        return redirect('medecin:medecin')
    return render(request, 'Medecin/supprimer_medecin.html', {'medecin': medecin})
