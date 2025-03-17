from django import forms
from django.core.exceptions import ValidationError
from .models import Cotisation

class CotisationForm(forms.ModelForm):
    class Meta:
        model = Cotisation
        fields = ['adherent', 'annee', 'montant']
        widgets = {
            'annee': forms.NumberInput(attrs={'min': 2000, 'max': 2100}),
            'date_paiement': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date_paiement(self):
        """ Validation au niveau du formulaire """
        date_paiement = self.cleaned_data.get('date_paiement')
        adherent = self.cleaned_data.get('adherent')

        if adherent and date_paiement and date_paiement < adherent.date_creation.date():
            raise ValidationError("La date de paiement doit être postérieure à la date de création de l'adhérent.")

        return date_paiement
