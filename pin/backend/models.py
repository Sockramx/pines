from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Pin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=180)

    def __str__(self):
        return self.name