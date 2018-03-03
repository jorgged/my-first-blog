from django.urls import path
from . import views



app_name = 'core'
urlpatterns = [
    path('home/',views.Home,name='home'),
    path('login/',views.LoginUser,name = 'login'),
    path('newuser/', views.NewUser, name='new_user'),
    path('newstudent/', views.NewStudent, name='new_student'),
    path('newsfacultad/', views.NewFacultad, name='new_facultad'),
]