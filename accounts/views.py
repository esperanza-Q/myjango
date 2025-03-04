from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1']
            )
            
            # Profile 추가 필드 저장
            nickname = request.POST['nickname']  # 사용자 입력받은 nickname
            userImage = request.FILES['userImage'] # 사용자 입력받은 userImage

            # Profile 모델에 저장
            profile = Profile.objects.create(
                user=user,
                nickname=nickname,
                userImage=userImage
            )
            auth.login(request, user)
            return redirect('home:home') # 여기서 도움말로 이동해야 됨.
        return render(request, 'test_signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
    return render(request, 'test_signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # 정보가 일치하지 않는 경우 none

        if user is not None:
            auth.login(request, user)
            return redirect('home:home')
        else:
            return render(request, 'test_login.html', {'error': 'username or password'})
    
    else:
        return render(request,'test_login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home:home')

def userDelete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth.logout(request)  # 로그아웃 처리
    return redirect('home:home')