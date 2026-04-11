from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    flyer = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name