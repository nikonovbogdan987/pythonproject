from django.urls impotr path
from . import views

urlpattens = [
    path('', views.helloworld, name='helloworld')
]