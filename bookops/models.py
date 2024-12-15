from django.contrib.auth.models import AbstractUser
from django.db import models

# Basic user with an editor flag set from registration
class User(AbstractUser):
    editor = models.BooleanField(default=False)



