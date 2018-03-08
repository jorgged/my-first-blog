from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('home/', views.Home, name='home'),
    path('login/', views.LoginUser, name='login'),
    path('newseccion/', views.NewSeccion, name='new_seccion'),
    path('newstudent/', views.NewStudent, name='new_student'),
    path('newcourse/', views.NewCourse, name='new_course'),
    path('newteacher/', views.NewTeacher, name='new_teacher'),

]
