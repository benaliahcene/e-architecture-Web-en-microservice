# gestion_chambres_app/models.py

from django.db import models
from django.contrib.auth.models import User

# gestion_chambres_app/models.py

from django.db import models
from django.contrib.auth.models import User

class Chambre(models.Model):
    id = models.AutoField(primary_key=True)  # Utilisation d'un champ id comme clé primaire
    type_chambre = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)  # Utilisation de l'id comme représentation textuelle


class Reservation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.chambre.id}"
