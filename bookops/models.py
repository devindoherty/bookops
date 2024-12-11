from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    editor = models.BooleanField(default=False)



