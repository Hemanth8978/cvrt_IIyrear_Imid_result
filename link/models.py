from django.db import models

# Create your models here.
class Result(models.Model):
    name=models.CharField(max_length=30)
    htn=models.CharField(max_length=15)
    mm=models.IntegerField()
    mres=models.CharField(max_length=10)
    obm=models.IntegerField()
    obres=models.CharField(max_length=10)
    osm=models.IntegerField()
    osre=models.CharField(max_length=10)
    dbmsm=models.IntegerField()
    dbmsres=models.CharField(max_length=10)
    sem=models.IntegerField()
    seres=models.CharField(max_length=10)
