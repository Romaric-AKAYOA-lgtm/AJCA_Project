from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import CV
from .forms import CVForm

# 🔹 Lister tous les CVs + Recherche avec plusieurs critères
def cv_list(request):
    query = request.GET.get('q', '')  # Récupération du paramètre de recherche
    cv_list = CV.objects.all()  # Tous les CVs par défaut

    if query:
        cv_list = cv_list.filter(
            Q(user__username__icontains=query) |  # Recherche par username
            Q(user__first_name__icontains=query) |  # Recherche par prénom
            Q(user__last_name__icontains=query) |  # Recherche par nom
            Q(titre__icontains=query)  # Recherche par titre du CV
        )

    return render(request, 'CV/cv_list.html', {'cv_list': cv_list, 'query': query})

# 🔹 Ajouter un nouveau CV
def cv_create(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user  # Associer le CV à l'utilisateur connecté
            cv.save()
            return redirect('CV:cv_list')
    else:
        form = CVForm()

    return render(request, 'CV/cv_form.html', {'form': form, 'action': 'Créer'})

# 🔹 Modifier un CV existant (Seulement l'utilisateur propriétaire du CV)
def cv_modifier(request, id):
    cv = get_object_or_404(CV, id=id, user=request.user)

    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES, instance=cv)
        if form.is_valid():
            form.save()
            return redirect('CV:cv_list')
    else:
        form = CVForm(instance=cv)

    return render(request, 'CV/cv_modifier.html', {'form': form, 'action': 'Modifier'})

# 🔹 Voir le détail d’un CV
def cv_detail(request, id):
    cv = get_object_or_404(CV, id=id)
    return render(request, 'CV/cv_detail.html', {'cv': cv})
