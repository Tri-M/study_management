from django.db import models

class Study(models.Model):
    PHASE_CHOICES = [
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),
    ]

    name = models.CharField(max_length=200)
    phase = models.CharField(max_length=20, choices=PHASE_CHOICES)
    sponsor = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        db_table = 'studies_study'

    def __str__(self):
        return self.name
