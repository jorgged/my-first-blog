from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import six

from .models import Student, Teacher, Course, Person, Student_inscription
from .forms import NewStudentForm, LoginForm, NewCourseForm, NewTeacherForm
from django.views.generic import ListView, FormView, CreateView


class Home(ListView):
    model = Course
    template_name = 'student/Home.html'


class LogoutUser(LogoutView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('core:home')



class NewCourse(CreateView):
    model = Course
    form_class = NewCourseForm
    success_url = reverse_lazy('core:home')
    template_name = 'student/NewCourse.html'


    def form_valid(self, form):
        form.save()
        return super(NewCourse, self).form_valid(form)


class Inscription(ListView):
    model = Course
    template_name = 'student/Inscription.html'


class Inscribir(CreateView):
    model = Student_inscription


    def json_to_response(self):
        data = dict()
        pk = self.kwargs.get('pk',None)
        user = self.request.user
        curso = get_object_or_404(Course, pk=pk)
        st = Student_inscription(
            student_exp= user.username,
            student_name= user.first_name,
            seccion= curso
        )
        st.save()
        curso.seats -= 1
        curso.save()
        data['inscrito'] = True
        materias = Course.objects.all()
        data['html_courses_list'] = render_to_string('student/includes/courses_list.html', {
            'materias': materias
        })
        return JsonResponse(data)


    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return self.json_to_response
        return self.render_to_response({})


class ListCourses(ListView):
    model = Student_inscription
    template_name = 'student/student_inscription_list.html'


class LoginUser(FormView):
    template_name = 'Login.html'
    form_class = LoginForm
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        usuario = authenticate(username=username, password=password)
        login(self.request,usuario)
        return super(LoginUser, self).form_valid(form)




class NewTeacher(CreateView):
    model = Person
    template_name = 'student/NewCourse.html'
    success_url = reverse_lazy('core:home')
    fields = ['first_name','last_name','email','adress','cellphone','phone','dni']

    def form_valid(self, form):
        import ipdb;ipdb.set_trace()
        teacher = form.save(commit=False)
        teacher.username = 'iec' + teacher.dni
        teacher.type_user = 'teacher'
        teacher.set_password(teacher.dni)
        teacher.save()
        # return self.render_to_response(self.get_context_data(form=form))
        return super(NewTeacher, self).form_valid(form)


class NewStudent(CreateView):
    model = Person
    template_name = 'student/NewStudent.html'
    success_url = reverse_lazy('core:home')
    fields = ['first_name', 'last_name', 'email', 'adress', 'cellphone', 'phone', 'dni']


    def form_valid(self, form):
        student = form.save(commit=False)
        student.username = 'iec' + student.dni
        student.set_password(student.dni)
        student.type_user = 'student'
        student.save()
        return self.render_to_response(self.get_context_data(form=form))