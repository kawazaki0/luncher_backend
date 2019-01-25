from django.db import models
from django.contrib.auth.models import AbstractUser
from restaurants.models import Location
from restaurants.models import Meal


class User(AbstractUser):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)