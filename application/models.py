from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    age= models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    staff = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
