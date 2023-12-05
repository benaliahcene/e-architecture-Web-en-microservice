from django.db import models

class User(models.Model):

        id= models.AutoField(primary_key= True)
        firstname=models.CharField(max_length=13)
        lastname= models.CharField(max_length=13)
        email=models.EmailField()
        dob= models.DateField()
        

