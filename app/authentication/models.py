from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(null=True, blank=True, default=False)
    is_superuser = models.BooleanField(null=True, blank=True, default=False)

