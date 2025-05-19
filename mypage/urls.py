from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import mypage, myref, ing_add

app_name='mypage'

urlpatterns = [
    path('', mypage, name='mypage'),
    path('myref/', myref, name='myref'),
    path('myref/ing_add/', ing_add, name='ing_add'),
]
