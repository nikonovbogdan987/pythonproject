from django.shortcuts import render
from .models import Clients, Orders
from django.conf import settings
# Create your views here.
def main(request):
    return render(request, 'main.html')
def pc(request):
    return render(request, 'PC.html')
def support(request):
    return render(request, 'support.html')
def console(request):
    return render(request, 'Console.html')
def page_of_registration(request):
        context = {}
        name = ''
        surname = ''
        email = ''
        phone = ''
        password = ''
        if request.method == 'POST' and 'login_btn' in request.POST:
            name = request.POST['username']
            surname = request.POST['usersurname']
            email = request.POST['useremail']
            phone = request.POST['userphonenumber']
            password = request.POST['userpassword']
            client = Clients()
            client.name = request.POST["username"]
            client.surname = request.POST["usersurname"]
            client.email = request.POST["useremail"]
            client.phone = request.POST["userphonenumber"]
            client.password = request.POST["userpassword"]
            client.save()
            settings.CURRENT_USER = client
            if not isinstance(settings.CURRENT_USER, str):
                context = {
                    "current_user" : settings.CURRENT_USER,
                    #"orders" : Orders.object.filter(author=settings.CURRENT_USER)
                }
            return render(request, 'main.html')
        return render(request, 'page_of_registration.html')



