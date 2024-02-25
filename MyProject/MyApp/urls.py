from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld, name='helloworld'),
    path('main_page', views.main_page, name='main_page'),
    path('comment', views.comment, name='commment'),
]