from django import forms
from django.forms.widgets import TextInput, PasswordInput
from .models import Student, Teacher, Facultad, Course
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class NewFacultadForm(forms.ModelForm):
    class Meta:
        model = Facultad
        fields = '__all__'


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']


class NewStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
