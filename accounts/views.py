from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import auth
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            
            user = CustomUser.objects.create_user(
                nickname = request.POST['nickname'],
                username = request.POST['username'],
                email = request.POST['email'],
                password = request.POST['password1'],
                user_image = request.FILES['user_image']
            )
            # 정보를 한꺼번에 담아 객체 생성 or post = Post()로 객체 먼저 생성해도 됨! 적절하게 사용.
            
            return render(request, 'login.html')   
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