from django.db import models

# Create your models here.
# models.py

from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    is_practical = models.BooleanField()

class Timeslot(models.Model):
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
class Meta:
        app_label = 'classmaster'