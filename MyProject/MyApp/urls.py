from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('support/', views.support, name='support'),
    path('Console/', views.console, name='Console'),
    path('PC/', views.pc, name='PC'),
    path('page_of_registration/', views.page_of_registration, name='page_of_registration'),
]