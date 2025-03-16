from django.db import models
from Adherent.models import Adherent
from tuteur.models import Tuteur

# Create your models here.
class TutteurAdherent(models.Model):
    tuteur = models.ForeignKey(Tuteur, on_delete=models.CASCADE)  # Renommé
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE)  # Renommé
    date_creation = models.DateTimeField(auto_now_add=True)