# rendezvous/forms.py
from django import forms
from .models import RendezVous

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['nom', 'prenom', 'email', 'telephone', 'avocat_choisi', 'date_heure']

