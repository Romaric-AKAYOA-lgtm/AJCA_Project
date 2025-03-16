from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Tuteur

class TuteurForm(forms.ModelForm):
    class Meta:
        model = Tuteur
        fields = [
            'last_name', 'first_name', 'date_naissance', 'lieu_naissance', 'lieu_residence', 
            'adresse', 'sexe', 'telephone', 'email', 'image'
        ]
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
            'sexe': forms.Select(choices=[('Masculin', 'Masculin'), ('Féminin', 'Féminin')]),
        }

    def clean(self):
        cleaned_data = super().clean()
        date_naissance = cleaned_data.get('date_naissance')
        date_creation = getattr(self.instance, 'date_creation', None)

        if date_creation and isinstance(date_creation, datetime):
            date_creation = date_creation.date()  # Conversion en date

        if date_naissance and date_creation and date_creation < date_naissance:
            self.add_error('date_naissance', "La date de naissance ne peut pas être après la date de création.")

        return cleaned_data

    # Méthode de sauvegarde pour vérifier les doublons
    def save(self, *args, **kwargs):
        # Récupérer les valeurs nettoyées
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        # Vérification des doublons sauf pour l'objet actuel
        if Tuteur.objects.filter(first_name=first_name, last_name=last_name).exclude(id=self.instance.id).exists():
            raise ValidationError(f"Un tuteur avec le même prénom et nom existe déjà.")
        
        # Sauvegarde de l'objet Tuteur
        return super(TuteurForm, self).save(*args, **kwargs)
