from rest_framework import serializers
from .models import Utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'


from rest_framework import serializers
from .models import Evaluation

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'

# serializers.py
from rest_framework import serializers
from .models import Avocat, RendezVous

class AvocatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avocat
        fields = '__all__'

