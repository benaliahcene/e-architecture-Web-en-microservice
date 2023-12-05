from django.db import models

class Vol(models.Model):

        id= models.AutoField(primary_key= True)
        company=models.CharField(max_length=13)
        price= models.BigIntegerField()
        aeroport_depart=models.DateField()
        aeroport_retour=models.DateField()
        date_aller=models.DateField()
        date_retour=models.DateField()
        

