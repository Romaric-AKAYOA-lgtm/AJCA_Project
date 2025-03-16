import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

# Fonction de validation pour empêcher l'utilisation de chiffres
def validate_no_numbers(value):
    if re.search(r'\d', value):
        raise ValidationError(f"Le champ ne peut pas contenir de chiffres.")

class User(models.Model):
    last_name = models.CharField(max_length=50, null=True, blank=False, validators=[validate_no_numbers])
    first_name = models.CharField(max_length=50, null=True, blank=True, validators=[validate_no_numbers])
    sexe = models.CharField(max_length=50, choices=[('Masculin', 'Masculin'), ('Féminin', 'Féminin')])
    date_naissance = models.DateField(null=True, blank=True)
    lieu_naissance = models.CharField(max_length=50, null=True, blank=True)
    lieu_residence = models.CharField(max_length=50, null=True, blank=True)
    adresse = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=40, unique=True, default='example@example.com')
    telephone = models.CharField(max_length=15, blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="1.png", upload_to='adherent/', blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name="custom_user_groups",
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="custom_user_permissions",
        blank=True
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_email_link(self):
        return f"<a href='mailto:{self.email}'>{self.email}</a>"

    def get_tel_link(self):
        return f"<a href='tel:{self.telephone}'>{self.telephone}</a>" if self.telephone else "Non spécifié"

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

