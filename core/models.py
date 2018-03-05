from django.contrib.auth.models import User
from django.db import models


class Facultad(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    exp = models.OneToOneField(User,models.SET_NULL, blank=True, null=True,)
    facultad = models.ForeignKey(Facultad, models.SET_NULL, blank=True, null=True,)
    dni = models.CharField(max_length=100)
    def __str__(self):
        return self.dni

class Teacher(models.Model):
    exp = models.OneToOneField(User,models.SET_NULL, blank=True, null=True,)
    dni = models.CharField(max_length=100)
    def __str__(self):
        return self.dni

class Course(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=500)
    seccion = models.CharField(max_length=100)
    estudent = models.ForeignKey(Student,models.SET_NULL, blank=True, null=True,)
    teacher = models.ForeignKey(Teacher,models.SET_NULL, blank=True, null=True,)
    period = models.CharField(max_length=100)
    score = models.CharField(max_length=5)

    def __str__(self):
        return self.name
