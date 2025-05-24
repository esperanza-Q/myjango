from django.db import models
from accounts.models import CustomUser
from recipe.models import Recipe

# Create your models here.
class UserIngredient(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amounts = models.IntegerField(null=False)
    UNIT_CHOICES = (
        ('g', 'g'),
        ('kg', 'kg'),
        ('ml', 'ml'),
        ('L', 'L'),
        ('개', '개'),
        ('마리', '마리')
    )
    unit = models.CharField(max_length=7, default='g', choices=UNIT_CHOICES, verbose_name="단위")
    icon = models.CharField(max_length=255, null=False, blank=False, default='img/재료아이콘/고기테스트.png')
    expiration_date = models.DateTimeField()

class Scrap(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # 폴더 이름

    def __str__(self):
        return f"{self.user.username}의 스크랩 폴더: {self.name}"


class ScrapRecipe(models.Model):
    scrap = models.ForeignKey(Scrap, on_delete=models.CASCADE, related_name='scrap_recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    add_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('scrap', 'recipe')  # 하나의 폴더에 중복 저장 방지

    def __str__(self):
        return f"{self.scrap.name} 폴더에 스크랩된 {self.recipe.title}"