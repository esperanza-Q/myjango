from django.db import models
from accounts.models import CustomUser

class Recipe(models.Model):
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=150)
    recipe_image = models.ImageField(upload_to="post_image/")