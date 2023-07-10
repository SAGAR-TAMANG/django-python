from django.db import models

# Create your models here.

class destination(models.Model):
    name= models.CharField(max_length = 150, unique=False, default='')
    sale= models.IntegerField(max_length = 10, unique=False, default='')
    offer= models.BooleanField(default = False, unique=False)