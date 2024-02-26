from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about_us/', views.about_us, name='about_us'),
    path('for_student/', views.for_student, name='for_student'),
    path('programs_and_courses/', views.programs_and_courses, name='programs_and_courses'),
    path('python/', views.python, name='python'),
    path('C_plus/', views.C_plus, name='C_plus'),
    path('web/', views.web, name='web'),
    path('support/', views.support, name='support'),
]