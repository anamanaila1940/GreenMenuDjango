from django.db import models
from items.models import Product

# Create your models here.

class MenuItems(models.Model):
    title = models.ForeignKey(Product, on_delete=models.CASCADE)

