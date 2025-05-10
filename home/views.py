from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def toSignup(request):
    return render(request, 'signup.html')

def toLogin(request):
    return render(request, 'login.html')