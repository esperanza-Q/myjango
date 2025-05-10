from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, toLogin, toSignup

app_name='home'

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', toLogin, name='toLogin'),
    path('signup/', toSignup, name='toSignup')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)