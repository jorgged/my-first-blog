from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Student, Teacher, Course, Person
from .forms import NewStudentForm, LoginForm, NewCourseForm, NewTeacherForm, NewSeccionForm


def Home(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'student/Home.html', ctx)


def NewStudent(request):
    if request.method == 'POST':
        form = NewStudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.username = 'iec'+ student.dni
            student.set_password(student.dni)
            student.type_user='student'
            student.save()
            return redirect('core:home')
    else:
        new_user_form = NewStudentForm()
        form = NewStudentForm()
        ctx = {'new_user_form': new_user_form, 'form': form}
    return render(request, 'student/NewStudent.html', ctx)


def LoginUser(request):
    mensaje = ''
    if request.user.is_authenticated:
        return redirect('core:home')
    else:
        if request.method == 'POST':
            next = request.POST
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return redirect('core:home')
                else:
                    mensaje = "Usuario o Password incorrectos!"
        form = LoginForm()
        next = request.GET
        ctx = {'form': form, 'mensaje': mensaje, 'next': next}
        return render(request, 'student/LoginStudent.html', ctx)


def NewCourse(request):
    if request.method=='POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = NewCourseForm()
        ctx = {'form':form}
    return render(request,'student/NewCourse.html',ctx)


def NewSeccion(request):
    if request.method == 'POST':
        form = NewSeccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = NewSeccionForm()
        ctx = {'form':form}
    return render(request,'student/NewSeccion.html',ctx)


def NewTeacher(request):
    if request.method=='POST':
        form = NewTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = NewTeacherForm()
        ctx = {'form':form}
    return render(request,'student/NewCourse.html',ctx)