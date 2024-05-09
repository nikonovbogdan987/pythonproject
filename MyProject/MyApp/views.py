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
    return render(request, 'page_of_registration.html')


