from django import forms
from .models import TutteurAdherent
class TuteurAdhenrentForm(forms.ModelForm):
    class Meta:
        model = TutteurAdherent
        fields = [
         'tuteur', 'adherent'
        ]
