from django.db import models
from accounts.models import CustomUser

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
