from django.db import models
from datetime import date
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField()
