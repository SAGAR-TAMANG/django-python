from django.db import models

# Create your models here.

class destination:
    name: models.CharField(max_length = 150)
    sale: models.IntegerField(max_length = 10)
    offer: models.BooleanField(default = False)
    offer2: models.BooleanField(default = False)