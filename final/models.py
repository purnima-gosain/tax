from django.db import models

# Create (your models here.
class Tax(models.Model):
    salary = models.IntegerField(blank=False,null=True)