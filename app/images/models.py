from django.db import models
from authentication.models import User


class Images(models.Model):
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)