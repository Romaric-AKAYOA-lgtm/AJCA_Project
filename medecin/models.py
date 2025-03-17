from django.db import models

# Create your models here.
from django.db import models
from user.models import User

class Medecin(User):
   statut = models.CharField(max_length=15, default='Medecint')
