from django.shortcuts import render

# Create your views here.
# rendezvous/views.py
from django.http import JsonResponse
from .forms import RendezVousForm
from django.contrib.auth.decorators import login_required
from  .models  import  *

from django.shortcuts import render

# Dans votre views.py de l'application rendezvous
from django.shortcuts import render
from django.http import JsonResponse

def rendezvous_form(request):
    if request.method == 'POST':
        # Récupérez les données du formulaire
        nom = request.POST['lastName']
        prenom = request.POST['firstName']
        email = request.POST['email']
        telephone = request.POST['phoneNumber']
        avocat_choisi_id = request.POST['selectedLawyer']
        date_heure = request.POST['selectedDateTime']

        # Enregistrez les données dans le modèle RendezVous
        # (N'oubliez pas d'importer le modèle RendezVous et Avocat)
        rendezvous = RendezVous(
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
            avocat_choisi=Avocat.objects.get(id=avocat_choisi_id),
            date_heure=date_heure,
        )
        rendezvous.save()

        # Réponse JSON pour indiquer le succès
        return JsonResponse({'success': True})

    return render(request, 'rendezvous_form.html')

from rest_framework import generics
from .models import Avocat, RendezVous
from .serializer import AvocatSerializer, RendezVousSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Avocat, RendezVous
import json


class RendezVousListCreate(generics.ListCreateAPIView):
    queryset = RendezVous.objects.all()
    serializer_class = RendezVousSerializer