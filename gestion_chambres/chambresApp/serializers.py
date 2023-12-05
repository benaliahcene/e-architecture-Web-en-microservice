from rest_framework import serializers
from .models import Chambre

class ChambreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chambre
        fields = ['adress', 'price', 'date_entre','date_sortie']
