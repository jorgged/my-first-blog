from django.template.context_processors import static
from django.urls import path

from moodle import settings
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.LoginUser.as_view(), name='login'),
    path('home/', views.Home.as_view(), name='home'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('newstudent/', views.NewStudent.as_view(), name='new_student'),
    path('newcourse/', views.NewCourse.as_view(), name='new_course'),
    path('newteacher/', views.NewTeacher.as_view(), name='new_teacher'),
    path('inscription/', views.Inscription.as_view(), name='inscription'),
    path('inscription/<str:pk>/', views.Inscribir.as_view(), name='inscribir'),
    path('listcourses/',views.ListCourses.as_view(),name = 'listcourses'),

]
