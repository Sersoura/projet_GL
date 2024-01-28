
from rest_framework import serializers
from .models import Avocat, RendezVous



class RendezVousSerializer(serializers.ModelSerializer):
    class Meta:
        model = RendezVous
        fields = '__all__'