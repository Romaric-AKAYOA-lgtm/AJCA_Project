from django import forms

from cotisation.models import Cotisation
from .models import PriseCharge

from datetime import datetime

class PriseChargeForm(forms.ModelForm):
    class Meta:
        model = PriseCharge
        fields = ['objet', 'traitement', 'adherent', 'medecin', 'date_prise_charge']
        widgets = {
            'date_prise_charge': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date_prise_charge(self):
        date_prise_charge = self.cleaned_data.get('date_prise_charge')
        adherent = self.cleaned_data.get('adherent')

        if adherent:
            # Vérifier si l'adhérent a une cotisation pour l'année en cours
            annee_prise_charge = date_prise_charge.year
            cotisation_existante = Cotisation.objects.filter(adherent=adherent, annee=annee_prise_charge).exists()

            if not cotisation_existante:
                raise forms.ValidationError(
                    f"L'adhérent n'a pas de cotisation pour l'année {annee_prise_charge}. "
                    "La prise en charge ne peut être enregistrée."
                )

        return date_prise_charge
