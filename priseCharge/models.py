from django.db import models
from Adherent.models import Adherent
from medecin.models import Medecin

# Création du modèle PriseCharge
class PriseCharge(models.Model):
    objet = models.CharField(max_length=50, blank=True, null=True, verbose_name="Objet")
    traitement = models.TextField(blank=True, null=True, verbose_name="Traitement")
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE, verbose_name="Adhérent")
    date_prise_charge = models.DateField(auto_now_add=True, verbose_name="Date de prise en charge")
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, verbose_name="Médecin")

    def __str__(self):
        return f"{self.objet} - {self.adherent} ({self.date_prise_charge})"

    class Meta:
        verbose_name = "Prise en charge"
        verbose_name_plural = "Prises en charge"
        ordering = ["-date_prise_charge"]
