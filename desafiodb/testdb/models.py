from django.db import models

class AdlTest(models.Model):
    campo1 = models.CharField(max_length=100)
    valor1 = models.IntegerField()
