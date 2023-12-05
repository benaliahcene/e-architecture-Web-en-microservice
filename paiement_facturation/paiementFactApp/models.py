from django.db import models

class Facture(models.Model):

        id= models.AutoField(primary_key= True)
        type_facture=models.CharField(max_length=13)
        montant= models.BigIntegerField()
        user= models.ForeignKey(name="User",on_delete=models.CASCADE)
        

