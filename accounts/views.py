from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.db import IntegrityError



def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = CustomUser.objects.create_user(
                    nickname = request.POST['nickname'],
                    username = request.POST['username'],
                    email = request.POST['email'],
                    password = request.POST['password1'],
                    user_image = request.FILES['user_image']
                )
                return render(request, 'login.html')   

            except IntegrityError:
                return render(request, 'signup.html', {'error': '이미 존재하는 사용자명입니다.'})
            
        return render(request, 'signup.html') 
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return render(request, 'signupfin.html')
        else:
            return render(request, 'login.html')
        
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('accounts:login')    