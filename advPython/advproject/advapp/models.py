from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Advance(models.Model):
    a_name=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.a_name