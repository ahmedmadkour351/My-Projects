from tkinter import CASCADE
from django.db import models


# Create your models here.


class Moive(models.Model):
    hall = models.CharField(max_length=50)
    movie = models.CharField(max_length=50)
    data = models.DateField()


class Guest(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)


class Reservation(models.Model):
    guest = models.ForeignKey(
        Guest, related_name='reservation', on_delete=models.CASCADE)
    movie = models.ForeignKey(
        Moive, related_name='reservation', on_delete=models.CASCADE)
