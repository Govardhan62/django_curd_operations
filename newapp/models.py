from django.db import models

# Create your models here.

class Member(models.Model):
    firstname =models.CharField(max_length=120)
    lastname =models.CharField(max_length=120)
    country =models.CharField(max_length=50)
    
