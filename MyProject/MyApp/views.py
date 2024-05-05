from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')
def PC(request):
    return render(request, 'PC.html')
def support(request):
    return render(request, 'support.html')
def Console(request):
    return(request, 'Console.html')


