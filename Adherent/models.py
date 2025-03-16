from django.db import models
from user.models import User

class Adherent(User):
   statut = models.CharField(max_length=15, default='Adherent')
