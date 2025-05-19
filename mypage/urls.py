from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import mypage, myref, ing_add, ing_detail, ing_delete, ing_update, scrap, scrap_addFolder, scrap_deleteFolder, scrap_detail

app_name='mypage'

urlpatterns = [
    path('', mypage, name='mypage'),
    # 마이냉장고-재료
    path('myref/', myref, name='myref'),
    path('myref/ing_add/', ing_add, name='ing_add'),
    path('myref/ing_detail/<int:ing_id>/', ing_detail, name='ing_detail'),
    path('myref/ing_detail/<int:ing_id>/delete/', ing_delete, name='ing_delete'),
    path('myref/ing_update/<int:ing_id>/', ing_update, name='ing_update'),
    #스크랩
    path('scrap/', scrap, name='scrap'),
    path('scrap/scrap_add/', scrap_addFolder, name='scrap_add'),
    path('scrap/scrap_delete/', scrap_deleteFolder, name='scrap_delete'),
    path('scrap/scrap_detail/<int:scrap_id>/', scrap_detail, name='scrap_detail'),
]
