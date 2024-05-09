from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('support/', views.support, name='support'),
    path('Console/', views.Console, name='Console'),
    path('PC/', views.PC, name='PC'),
    path('page_of_registration/', views.page_of_registration, name='page_of_registration'),
]