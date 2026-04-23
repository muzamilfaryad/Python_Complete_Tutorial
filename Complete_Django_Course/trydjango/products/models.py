from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #max_length is required for CharField
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    summary = models.TextField(blank=True, null=True)
    featured = models.BooleanField(null=True, default=None) #null=true means it can be true, false or null , default is null