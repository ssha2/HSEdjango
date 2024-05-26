from django.db import models

class Surmodel(models.Model):
    frequency= models.CharField( max_length=100)
    partday= models.CharField( max_length=100)
    prefsport= models.CharField( max_length=100)
    consume= models.CharField( max_length=100)
    prodtype= models.CharField( max_length=100)
    bodytype= models.CharField( max_length=100)
    sex= models.CharField( max_length=100)
    age= models.IntegerField()
    email= models.CharField( max_length=100)
    comment= models.CharField( max_length=100)

