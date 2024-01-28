# authentification/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

# authentification/models.py

class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_avocat = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    # Ajoutez d'autres champs utilisateur si nécessaire


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Ajoutez d'autres champs spécifiques à l'admin si nécessaire

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    preferred_language = models.CharField(max_length=50, null=True, blank=True)


class Avocat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=500, default='Valeur par défaut')
    specialite = models.CharField(max_length=100, null=True, blank=True)
    coordinates = models.CharField(max_length=255, null=True, blank=True)
    langue = models.CharField(max_length=50, null=True, blank=True)
    experiences = models.TextField(null=True, blank=True)
    
    # Ajoutez d'autres champs spécifiques aux avocats (compétences, éducation, etc.)

from django.db import models
from .models import Avocat

class Comment(models.Model):
    avocat = models.ForeignKey(Avocat, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.avocat} at {self.created_at}"
