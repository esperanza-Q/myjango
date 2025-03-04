from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# recipe_write : title, content --> 작성 완료 버튼 // 
# recipe_detail : 수정 버튼 --> 수정 후 recipe_update

class RecipeWrite(models.Model):
    recipe_writer = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_title = models.CharField(max_length=400)
    recipe_content = models.TextField()
    # recipe_ingre = models.TextField()
    # recipe_per = models.IntegerField()  임의로 정한 거라 마음껏 바꾸셔도 됩니다.
    
    #디자인한 대로 틀은 만들어두자 (재료, 몇 인분)
    
    def __str__(self):
        return self.recipe_title
    
class RecipeImage(models.Model):
    write =models.ForeignKey(RecipeWrite, null=True, blank=True, on_delete=models.CASCADE)
    recipe_image = models.ImageField(upload_to="recipe_image/", blank=True, null=True)
    # 많은 이미지를 받아야 할 때 RecipeWrite와 외래키로 연결해서 따로 데베에 저장

    def __str__(self):
        return self.write.recipe_title