from django.urls impotr path
from . import views

urlpatterns = [
    path('', views.helloworld, name='helloworld'),
]