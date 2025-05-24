from django.db import models
from accounts.models import CustomUser

class Recipe(models.Model):
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=150)
    recipe_image = models.ImageField(upload_to="post_image/")

    
class RecipeIngredient(models.Model):
    recipe_id = models.ForeignKey(Recipe, related_name="ingredients", on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    amount = models.IntegerField(null=False)
    
    UNIT_CHOICES = (
        ('g', 'g'),
        ('kg', 'kg'),
        ('ml', 'ml'),
        ('L', 'L'),
        ('개', '개'),
        ('마리', '마리')
    )
    
    unit = models.CharField(max_length=7, default='g', choices=UNIT_CHOICES, verbose_name="단위")

