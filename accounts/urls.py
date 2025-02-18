from django.urls import path, include
from .views import signup, login, logout, userDelete
from django.conf import settings


app_name = "accounts"
# django가 써진 앱 이름을 사용해서 특정 앱의 URL을 명확히
# 구분할 수 있다.  ex) {% url 'accounts:login' %} 여기서의 accounts를 의미
# 앱 간 URL 충돌 방지를 위해 한 번 더 써준다!

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('userDelete/', userDelete, name='userDelete')
]