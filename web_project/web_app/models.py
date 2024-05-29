from django.db import models

class Surmodel(models.Model):
    frequency= models.CharField( max_length=100)
    partday= models.CharField( max_length=100)
    prefsport= models.CharField( max_length=500)
    consume= models.CharField( max_length=100)
    prodtype= models.CharField( max_length=500)
    bodytype= models.CharField( max_length=100)
    sex= models.CharField( max_length=100)
    age= models.IntegerField()
    email= models.CharField( max_length=100)
    comment= models.CharField( max_length=100)


class Catalog(models.Model):
    img= models.CharField( max_length=500)
    sch= models.CharField( max_length=500)
    name=models.CharField( max_length=100)
    desc= models.CharField( max_length=500)
    def __str__(self):
        return f"{self.name}"
    




