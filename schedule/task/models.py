from django.db import models

# Create your models here.
class tasks(models.Model):
    task = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)