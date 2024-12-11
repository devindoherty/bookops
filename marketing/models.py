from django.db import models
from bookops.models import User

# Create your models here.

class Lead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leads")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    marketing_type = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
