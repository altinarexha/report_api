from audioop import reverse
from django.db import models
from django.forms import DateField
from django.urls import reverse
# Create your models here.

class Task(models.Model):
    content=models.CharField(max_length=100)
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id
