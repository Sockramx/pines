from django.db import models

# Create your models here.
class Pin(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=180)

    def __str__(self):
        return self.name