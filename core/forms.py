from django import forms
from django.forms import PasswordInput, TextInput
from .models import Student, Teacher, Course, Person


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())



class NewCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'



class NewStudentForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','last_name','email','adress','cellphone','phone','dni']
        #exclude = ['is_superuser','is_staff','date_joined','type_user','user_permissions','groups','last_login']
        widgets = {
            'cellphone': TextInput(),
            'phone': TextInput(),
            'password': PasswordInput(render_value=False),
        }
        labels = {
            'password': 'Clave',
        }
        help_texts = {
            'password': 'Aqui va la clave',
        }


class NewTeacherForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','last_name','email','adress','cellphone','phone','dni']
        #exclude = ['is_superuser','is_staff','date_joined','type_user','user_permissions','groups','last_login']
        widgets = {
            'cellphone': TextInput(),
            'phone': TextInput(),
            'password': PasswordInput(render_value=False),

        }
        labels = {
            'password': 'Clave',
        }
        help_texts = {
            'password': 'Aqui va la clave',
        }


