from django.db import models

# Create your models here.


class Staff(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=10)
    subject = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    noofstudent = models.IntegerField()


class Student(models.Model):
    teacher = models.CharField(max_length=30)
    rollno = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=5)
    subject = models.CharField(max_length=30)
    mark = models.IntegerField()
