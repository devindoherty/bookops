from django.db import models
from bookops.models import User
from manuscript.models import Manuscript

# Create your models here.

class Lead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leads")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    marketing_type = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Sale(models.Model):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE, related_name="sales")
    buyer = models.ForeignKey("Buyer", on_delete=models.CASCADE, related_name="buys")
    online = models.BooleanField(default=True)
    location = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

class Buyer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)