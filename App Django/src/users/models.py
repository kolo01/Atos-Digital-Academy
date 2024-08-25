from django.db import models

# Create your models here.
class User(models.Model):

    pseudos = models.CharField(max_length=10,unique=True,)
    password = models.CharField(max_length=120,null=True)
    creat_at = models.DateTimeField(auto_now_add=True)