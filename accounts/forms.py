from django.db import forms
from django.contrib.auth.models import UserCreationForm
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('nickname', 'username', 'email', 'password1', 'password2') 
        # 리스트도 괜찮지만 튜플이 더 안전함.