from django.urls import path
from .views import test_home

app_name = 'home'

urlpatterns = [
    # path('home/', home, name='home'),
    path('test_home/', test_home, name='test_home')
]