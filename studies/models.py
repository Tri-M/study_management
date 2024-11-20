from django.db import models

class Study(models.Model):
    name = models.CharField(max_length=255)  
    phase = models.CharField(max_length=255, default='Phase I')
    sponsor = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
