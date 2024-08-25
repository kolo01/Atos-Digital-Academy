from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1)
    matricule = models.CharField(max_length=20)
    courses = models.CharField(max_length=15)
    number = models.CharField(max_length=10)
    ville = models.CharField(max_length=20)