from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from tuteur.models import Tuteur
from django.urls import reverse
from .models import Adherent
from .forms import AdherentForm


def adherent_list(request):
    adherents = Adherent.objects.all().order_by("-date_creation")
    return render(request, 'Adherent/adherent_list.html', context={'adherents': adherents})

def adherent_create(request):
    form = AdherentForm()
    if request.method == 'POST':
        form = AdherentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Adherent:Adherent'))
        else:
            print(form.errors)
    return render(request, 'Adherent/adherent_create.html', context={'form': form})

def adherent_detail(request, id):
    adherent = get_object_or_404(Adherent, id=id)
    return render(request, 'Adherent/adherent_detail.html', {'adherent': adherent})

def modifier_adherent(request, id):
    adherent = get_object_or_404(Adherent, id=id)
    if request.method == 'POST':
        form = AdherentForm(request.POST, instance=adherent)
        if form.is_valid():
            form.save()
            return redirect('Adherent:Adherent')
    else:
        form = AdherentForm(instance=adherent)
    return render(request, 'Adherent/modifier_adherent.html', {'form': form, 'adherent': adherent,})

def supprimer_adherent(request, id):
    adherent = get_object_or_404(Adherent, id=id)
    if request.method == 'POST':
        adherent.delete()
        return redirect('Adherent:Adherent')
    return render(request, 'Adherent/supprimer_adherent.html', {'adherent': adherent})
