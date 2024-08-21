from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Material(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)