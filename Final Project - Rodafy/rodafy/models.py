from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    pass

class Parking_Space(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, default=None)
    title = models.CharField(default=None, max_length=40)
    length = models.IntegerField(default=None)
    width = models.IntegerField(default=None)
    address = models.CharField(default=None, max_length=140)
    price = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    amount_vehicles_allowed = models.IntegerField(default=None)
    amount_vehicles_current = models.IntegerField(default="0", null=True, blank=True)
    description = models.CharField(default=None, max_length=500)
    created = models.DateTimeField(default=datetime.now())


def __str__(self):
        return str(self.parking_space)

class Message(models.Model):
    sender = models.ForeignKey("User", on_delete=models.PROTECT, related_name="messages_sent")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="messages")
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
