from django.db import models

# Create your models here.

class Product(models.Model):
    CATEGORY=(
        ('GF', 'GF'),
        ('V', 'V'),
        ('VG','VG'),
        ('No','No'),
    )

    TYPE = (
        ('Starters','Starters'),
        ('Pizza','Pizza'),
        ('Sides','Sides'),
        ('Dessert','Dessert'),
       
    )

    STATUS  = (
        ('In date', 'In date'),
        ('Out of date', 'Out of date'),
        ('Available','Available'),
        ('Unavailable', 'Unavailable'),
    )
    MISTAKE = (
        ('Mistake', 'Mistake'),
        ('No mistake', 'No mistake'),
    )
    mistake = models.CharField(max_length=200, null=True, choices = MISTAKE)
    quantity = models.FloatField(null=True)
    status = models.CharField(max_length=200, null=True, choices = STATUS)
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices = CATEGORY)
    type = models.CharField(max_length=200, null=True, choices = TYPE)
    image = models.ImageField(null=True, blank=True, upload_to="static/images")
    description = models.CharField(max_length=500, null = True)
    price = models.FloatField(null=True)
    mistakeprice = models.FloatField(null=True)
    allergens = models.CharField(max_length=200, null=True)
    idnum = models.FloatField(null=True)
    def __str__(self):
        return self.name
    

class LocalGoods(models.Model):
    CATEGORY=(
        ('GF', 'GF'),
        ('V', 'V'),
        ('VG','VG'),
        ('No','No'),
    )
    STATUS  = (
        ('In date', 'In date'),
        ('Out of date', 'Out of date'),
        ('Available','Available'),
        ('Unavailable', 'Unavailable'),
    )
    MISTAKE = (
        ('Mistake', 'Mistake'),
        ('No mistake', 'No mistake'),
    )
    mistake = models.CharField(max_length=200, null=True, choices = MISTAKE)
    quantity = models.FloatField(null=True)
    status = models.CharField(max_length=200, null=True, choices = STATUS)
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices = CATEGORY)
    image = models.ImageField(null=True, blank=True, upload_to="static/images")
    description = models.CharField(max_length=500, null = True)
    price = models.FloatField(null=True)
    allergens = models.CharField(max_length=200, null=True)
    idnum = models.FloatField(null=True)
    def __str__(self):
        return self.name

    
        
