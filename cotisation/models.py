from django.db import models
from Adherent.models import Adherent

class Cotisation(models.Model):
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE, related_name="cotisations")
    annee = models.IntegerField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('adherent', 'annee')  # Un adhérent ne peut payer qu'une seule cotisation par an

    def __str__(self):
        return f"Cotisation {self.annee} - {self.adherent.nom} {self.adherent.prenom}"
