from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateTimeField()


class Product_v1(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    content = models.TextField(blank=True)
