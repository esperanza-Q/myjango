from django.urls import path
from .views import recipe_write, recipe_detail, recipe_delete, recipe_update

app_name = 'recipe'

urlpatterns = [
    # 레시피 작성/디테일/삭제/수정(업데이트)
    path('recipe_write/', recipe_write, name='recipe_write'),
    path('recipe_detail/<int:recipe_post_id>/', recipe_detail, name='recipe_detail'),
    path('recipe_detail/<int:recipe_post_id>/recipe_delete/', recipe_delete, name='recipe_delete'),
    path('recipe_detail/<int:recipe_post_id>/recipe_update/', recipe_update, name='recipe_update')
]