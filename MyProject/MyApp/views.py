from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')
def for_student(request):
    return render(request, 'for_student.html')
def about_us(request):
    return render(request, 'about_us.html')
def programs_and_courses(request):
    return render(request, 'programs_and_courses.html')
def support(request):
    return render(request, 'support.html')
def python(request):
    return(request, 'python.html')
def C_plus(request):
    return(request, 'C_plus.html')
def web(request):
    return(request, 'web.html')

