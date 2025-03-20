from django.db import models

# Create your models here.
from django.db import models
from specialite.models import Specialite
from user.models import User

class Medecin(User):
   statut = models.CharField(max_length=15, default='Medecint')
   specialite= models.ForeignKey(Specialite, on_delete=models.CASCADE)  # Renommé
  