from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import mypage, myref, ing_add, ing_detail, ing_delete, ing_update

app_name='mypage'

urlpatterns = [
    path('', mypage, name='mypage'),
    path('myref/', myref, name='myref'),
    path('myref/ing_add/', ing_add, name='ing_add'),
    path('myref/ing_detail/<int:ing_id>/', ing_detail, name='ing_detail'),
    path('myref/ing_detail/<int:ing_id>/delete/', ing_delete, name='ing_delete'),
    path('myref/ing_update/<int:ing_id>/', ing_update, name='ing_update'),
]
