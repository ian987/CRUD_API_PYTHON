from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publish_date = models.DateField(null=False)
    created = models.DateTimeField(default=timezone.now) 
    updated = models.DateTimeField(auto_now=True) # auto_now: changes everytime we save any of the fields
    