from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    scolarship = models.CharField(max_length=5)
    matricule = models.CharField(max_length=15,default=True)
    
