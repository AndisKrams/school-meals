from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Meal(models.Model):
    meal_date = models.DateField(unique=True)
    meal_choice1 = models.CharField(max_length=200)
    meal_choice2 = models.CharField(max_length=200)
    meal_choice3 = models.CharField(max_length=200, blank=True)
    meal_choice4 = models.CharField(max_length=200, blank=True)