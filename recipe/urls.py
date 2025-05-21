from django.urls import path
from .views import create, detail, recipe_list
from django.conf import settings
from django.conf.urls.static import static

app_name = 'recipe'

urlpatterns = [
    path('create/', create, name='create'),
    path('detail/<int:recipe_id>', detail, name='detail'),
    #테스트 리스트 url
    path('', recipe_list, name='recipe_list'),
]
