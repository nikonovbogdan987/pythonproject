from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('support/', views.support, name='support'),
    path('Console/', views.Console, name='Console'),
    path('PC/', views.PC, name='PC')
]