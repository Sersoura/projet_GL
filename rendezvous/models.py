from django.db import models

# Create your models here.
# rendezvous/models.py
from django.db import models
from django.contrib.auth.models import User
from authentification.models import *

class RendezVous(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    avocat_choisi = models.ForeignKey(Avocat, on_delete=models.CASCADE)
    date_heure = models.DateTimeField()
    # Ajoutez d'autres champs spécifiques aux rendez-vous
