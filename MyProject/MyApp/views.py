from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')
def PC(request):
    return render(request, 'PC.html')
def support(request):
    return render(request, 'support.html')
def Console(request):
    return render(request, 'Console.html')
def page_of_registration(request):
        name = ''
        surname = ''
        email = ''
        phone = ''
        password = ''
        if request.method == 'POST' and 'login_btn' in request.POST:
            name = request.POST['username']
            surname = request.POST['usersurname']
            email = request.POST['useremail']
            phonenumber = request.POST['userphonenumber']
            password = request.POST['userpassword']
        context = {
            'name' : name,
            'surname' : surname,
            'email' : email,
            'phone' : phone,
            'password' : password
        }
        return render(request, 'page_of_registration.html', context)


