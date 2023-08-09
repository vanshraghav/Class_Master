from django.db import models

# models.py

from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    # Other fields as needed

class Class(models.Model):
    name = models.CharField(max_length=100)
    # Other fields as needed

class Subject(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    practical_lectures = models.BooleanField()
    practical_batches = models.IntegerField()

class Timetable(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    # Other fields like day, time, etc.
