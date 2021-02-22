from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.TextField(null=False)
    done = models.BooleanField(default=False)
