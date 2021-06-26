from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path('test/', views.home, name="home"),
    path('teacher/', views.teacher, name="staff"),
    path('result/', views.result, name="result"),
    path('enroll/', views.enroll, name="enroll"),
    path('login/', views.login, name="login"),
    path('studentlogin/', views.student, name="student"),
    path('mark/<int:i>/', views.mark, name="mark"),
]
