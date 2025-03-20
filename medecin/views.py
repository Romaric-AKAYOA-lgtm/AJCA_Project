from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from specialite.models import Specialite
from .models import Medecin
from .forms import MedecinForm

def medecin_list(request):
    medecins = Medecin.objects.all().order_by("-date_creation")
    return render(request, 'medecin/medecin_list.html', context={'medecins': medecins})

def medecin_create(request):
    specialite = Specialite.objects.all().order_by("designation")
    form = MedecinForm()
    if request.method == 'POST':
        form = MedecinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('medecin:medecin'))
        else:
            print(form.errors)
    return render(request, 'medecin/medecin_create.html', context={'form': form, 'specialite':specialite})

def medecin_detail(request, id):
    medecin = get_object_or_404(Medecin, id=id)
    return render(request, 'medecin/medecin_detail.html', {'medecin': medecin})

def modifier_medecin(request, id):
    specialite = Specialite.objects.all().order_by("designation")
    medecin = get_object_or_404(Medecin, id=id)
    if request.method == 'POST':
        form = MedecinForm(request.POST, instance=medecin)
        if form.is_valid():
            form.save()
            return redirect('medecin:medecin')
    else:
        form = MedecinForm(instance=medecin)
    return render(request, 'medecin/modifier_medecin.html', {'form': form, 'medecin': medecin, 'specialite':specialite})

def supprimer_medecin(request, id):
    medecin = get_object_or_404(Medecin, id=id)
    if request.method == 'POST':
        medecin.delete()
        return redirect('medecin:medecin')
    return render(request, 'eedecin/supprimer_medecin.html', {'medecin': medecin})
