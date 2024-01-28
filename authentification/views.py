from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from allauth.socialaccount import providers
from allauth.socialaccount.models import SocialAccount
from django.http import HttpResponse

# evaluations/views.py
from rest_framework import generics
from .models import Evaluation
from .serializer import EvaluationSerializer
from rest_framework import viewsets
from .models import Utilisateur
from .serializer  import UtilisateurSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


class EvaluationListCreate(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer


def google_auth(request):
    provider = providers.registry.by_id("google")
    return redirect(provider.get_login_url(request, **{}))

def google_auth_callback(request):
    # Gérer le callback de Google ici
    # Vous pouvez récupérer les détails de l'utilisateur avec SocialAccount
    # Exemple : SocialAccount.objects.get(user=request.user).extra_data
    return HttpResponse("Google auth callback")

# views.py
# authentification/views.py
from django.shortcuts import render
from .models import Avocat

def avocat_list(request):
    avocats = Avocat.objects.all()
    return render(request, 'authentification/avocat_list.html', {'avocats': avocats})

# views.py
from django.shortcuts import render
from django import forms
from .models import Avocat

class AvocatSearchForm(forms.ModelForm):
    class Meta:
        model = Avocat
        fields = ['specialite', 'coordinates', 'langue']

def search_avocats(request):
    form = AvocatSearchForm(request.GET)
    avocats = []

    if form.is_valid():
        # Filtrer les avocats en fonction des critères du formulaire
        avocats = Avocat.objects.filter(
            specialite=form.cleaned_data['specialite'],
            coordinates=form.cleaned_data['coordinates'],
            langue=form.cleaned_data['langue'],
            # Ajoutez d'autres filtres en fonction des champs du modèle
        )

    response = f"Formulaire de recherche :\n{form}\n\n"

    if avocats:
        response += "Résultats :\n"
        for avocat in avocats:
            response += f"{avocat.nom} - {avocat.specialite} - {avocat.coordinates} - {avocat.langue}\n"
    else:
        response += "Aucun résultat trouvé."

    return HttpResponse(response)

   # views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Avocat
import json

@csrf_exempt
def inscription_avocat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Vérifiez les données et créez un nouvel avocat
        try:
            nouvel_avocat = Avocat.objects.create(
                nom=data['nom'],
                prenom=data['prenom'],
                email=data['email'],
                adresse=data['adresse'],
                specialite=data['specialite'],
                mot_de_passe=data['motDePasse']
            )
            return JsonResponse({'message': 'Inscription réussie'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'message': 'Méthode non autorisée'}, status=405)



@csrf_exempt
def create_appointment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Récupérer les données du formulaire
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        address = data.get('address')
        email = data.get('email')
        phone_number = data.get('phoneNumber')
        selected_lawyer = data.get('selectedLawyer')
        selected_date = data.get('selectedDate')
        selected_time = data.get('selectedTime')

        # Créer un nouveau rendez-vous dans la base de données
        try:
            rendezvous = rendezvous.objects.create(
                first_name=first_name,
                last_name=last_name,
                address=address,
                email=email,
                phone_number=phone_number,
                selected_lawyer=selected_lawyer,
                selected_date=selected_date,
                selected_time=selected_time
            )
            return JsonResponse({'message': 'Rendez-vous créé avec succès'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
    

def login_view(request):
    if request.method == 'POST':
        # Récupérer les données de la demande POST
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Ajouter votre logique de validation et d'authentification ici
        # Vérifier l'email et le mot de passe, authentifier l'utilisateur, etc.
        
        # Exemple de réponse pour le moment
        if email == 'test@example.com' and password == 'password':
            return JsonResponse({'message': 'Connexion réussie'})
        else:
            return JsonResponse({'error': 'Identifiants incorrects'}, status=400)
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

# Emplacement : votre_application/views.py
from rest_framework import viewsets
from .models import Avocat
from .serializer import AvocatSerializer

class AvocatViewSet(viewsets.ModelViewSet):
    queryset = Avocat.objects.all()
    serializer_class = AvocatSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', None)
        if search_term:
            queryset = queryset.filter(nom__icontains=search_term)  # Filtrer par nom (ou tout autre champ pertinent)
        return queryset
