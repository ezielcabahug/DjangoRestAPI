from django.db import models
from datetime import datetime


class Cars(models.Model):
    brand = models.CharField(max_length=30)
    model = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
