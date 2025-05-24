from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=15)
    user_image = models.ImageField(upload_to='user_images/')
    
    def __str__(self):
        return self.nickname