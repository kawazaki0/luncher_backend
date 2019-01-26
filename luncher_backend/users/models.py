from django.db import models
from django.contrib.auth.models import AbstractUser
from restaurants.models import Meal


class Location(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table='location'


class User(AbstractUser):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
