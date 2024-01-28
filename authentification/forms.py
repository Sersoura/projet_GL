# forms.py
from django import forms
from .models import Avocat
from .models import Comment

class AvocatSearchForm(forms.ModelForm):
    class Meta:
        model = Avocat
        fields = ['specialite', 'coordinates', 'langue']
        # Ajoutez d'autres champs du modèle Avocat pour la recherche avancée




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['rating', 'content']
