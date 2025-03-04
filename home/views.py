from django.shortcuts import render
from accounts.models import Profile

def home(request):
    profile = None
    if request.user.is_authenticated:
        # 현재 로그인된 사용자의 프로필 가져오기
        profile = Profile.objects.filter(user_id=request.user.id).first()  # 없을 경우 None 반환
    return render(request, 'test_home.html', {'profile': profile})