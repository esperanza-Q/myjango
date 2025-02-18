from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # django 기본 모델 User와 연결하는 외래키
    # settings.AUTH_USER_MODEL은 자동으로 auth.User로 설정된다.
    
    nickname = models.CharField(max_length=10)
    
    userImage = models.ImageField(upload_to="profile_image/", blank=True, null=True)
    # null=True : 데베에 해당 필드를 빈 값으로 저장할 수 있게 함
    # blank=True : 사용자가 빈 값으로 폼을 제출해도 에러 X, 빈 문자열 ""로 저장된다.
    
    def __str__(self):
        return self.nickname