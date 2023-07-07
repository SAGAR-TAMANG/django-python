from django.db import models

# Create your models here.
class Form(models.Model):
  naukri = models.CharField(max_length = 80)

  def __str__(self):
    return "f{self.naukri}"