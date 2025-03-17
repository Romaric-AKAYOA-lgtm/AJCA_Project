from django.db import models
from django.contrib.auth.models import User

class CV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cv')
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    fichier_cv = models.FileField(upload_to='cv_uploads/', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CV de {self.user.username}"
