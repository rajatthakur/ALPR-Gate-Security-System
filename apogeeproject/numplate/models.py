from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CarPlate(models.Model):
    numplate = models.CharField(max_length=20)
    inTime = models.DateTimeField()
    outTime = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.numplate