from django.shortcuts import render

# Create your views here.
def helloworld(request):
    return render(request, 'helloworld.html')
def main_page(request):
    return render(request, 'main_page.html')
def comment(request):
    return render(request, 'comment.html')