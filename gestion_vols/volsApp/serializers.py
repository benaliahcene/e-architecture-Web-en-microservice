from rest_framework import serializers
from .models import Vol

class VolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vol
        fields = ['company', 'price', 'aeroport_depart','aeroport_retour','date_aller','date_retour']
 