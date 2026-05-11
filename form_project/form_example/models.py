from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField()
    website = models.URLField()
    email = models.EmailField()