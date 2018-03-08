from django.db import models
from django.contrib.auth.models import AbstractUser



class Person(AbstractUser):
    adress = models.CharField(max_length=100)
    cellphone = models.IntegerField()
    phone = models.IntegerField()
    dni = models.CharField(max_length=100)

    # photo = models.ImageField() aun no lo configuro para despues


    student = 'student'
    teacher = 'teacher'
    type_user_options = (
        (student, 'student'),
        (teacher, 'teacher'),
    )
    type_user = models.CharField(max_length=30, choices=type_user_options)



class Teacher(models.Model):
    exp = models.CharField(max_length=30)  # username para el login
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    password = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    cellphone = models.IntegerField()
    phone = models.IntegerField()
    dni = models.CharField(max_length=100)
    # photo = models.ImageField() aun no lo configuro para despues
    is_active = models.BooleanField()

    def __str__(self):
        return self.name, self.last_name



class Student(models.Model):
    exp = models.CharField(max_length=30)  # username para el login
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    password = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    cellphone = models.IntegerField()
    phone = models.IntegerField()
    dni = models.CharField(max_length=100)
    career = models.CharField(max_length=500)

    # photo = models.ImageField() aun no lo configuro para despues
    is_active = models.BooleanField()

    def __str__(self):
        return self.name, self.last_name


class Course(models.Model):
    code = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=500)

    def __str__(self):
        texto = self.code+'_'+ self.name
        return texto


class Seccion(models.Model):
    course = models.ForeignKey(Course,on_delete=models.PROTECT)
    code = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    teacher_exp = models.CharField(max_length=30)
    teacher_name = models.CharField(max_length=30)
    teacher_last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.code


class student_inscription(models.Model):
    seccion = models.ForeignKey(Seccion,models.PROTECT)
    student_exp = models.CharField(max_length=30)
    student_name = models.CharField(max_length=30)

    def __str__(self):
        return self.student_exp