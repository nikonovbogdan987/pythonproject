from django.shortcuts import render
from .models import Clients

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
            context = {
                'name' : name,
                'surname' : surname,
                'email' : email,
                'phone' : phone,
                'password' : password
            }
            client = Clients()
            client.name = request.POST["username"]
            client.surname = request.POST["usersurname"]
            client.email = request.POST["useremail"]
            client.phone = request.POST["userphonenumber"]
            client.password = request.POST["userpassword"]
            client.save()
            return render(request, 'main.html')
        return render(request, 'page_of_registration.html')



