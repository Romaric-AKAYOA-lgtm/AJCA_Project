from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from Adherent.models import Adherent
from tuteur.models import Tuteur

from .models import TutteurAdherent
from .forms import TuteurAdhenrentForm

def tuteurAdherent_list(request):
    tuteurAdherent = TutteurAdherent.all().order_by("-date_creation")
    return render(request, 'tuteurAdherent/tuteurAdherent_list.html', context={'tuteurAdherent':tuteurAdherent})

def tuteurAdherent_create(request):
    tuteurs = Tuteur.objects.all().order_by('last_name')
    adherent=Adherent.objects.all().order_by('last_name')
    form = TuteurAdhenrentForm()
    if request.method == 'POST':
        form = TuteurAdhenrentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tuteurAdherent:tuteurAdherent'))
        else:
            print(form.errors)
    return render(request, 'tuteurAdherent/tuteurAdherent_create.html', context={'form': form, 'tuteurs': tuteurs, 'adherent':adherent})

def  tuteurAdherentt_detail(request, id):
    tuteurAdherent  = get_object_or_404(TutteurAdherent, id=id)
    return render(request, 'tuteurAdherent/tuteurAdherent_detail.html', {'tuteurAdherent':tuteurAdherent})

def modifier_tuteurAdherent(request, id):
    tuteurAdherent   = get_object_or_404(TutteurAdherent, id=id)
    tuteurs = Tuteur.objects.all().order_by('last_name')
    adherent=Adherent.objects.all().order_by('last_name')
    if request.method == 'POST':
        form = TuteurAdhenrentForm(request.POST, instance=tuteurAdherent)
        if form.is_valid():
            form.save()
            return redirect('tuteurAdherent:tuteurAdherent ')
    else:
        form = TuteurAdhenrentForm(instance=tuteurAdherent )
    return render(request, 'Adherent/modifier_adherent.html',  context={'form': form, 'tuteurs': tuteurs, 'adherent':adherent})

def supprimer_tuteurAdherent(request, id):
    tuteurAdherent   = get_object_or_404(TutteurAdherent, id=id)
    if request.method == 'POST':
        TutteurAdherent.delete()
        return redirect('tuteurAdherent:tuteurAdherent')
    return render(request, 'tuteurAdherent/supprimer_tuteurAdherent.html', {'tuteurAdherent':tuteurAdherent})
