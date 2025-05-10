from django.urls import path
from .views import create, detail
from django.conf import settings
from django.conf.urls.static import static

app_name = 'recipe'

urlpatterns = [
    path('create/', create, name='create'),
    path('detail/<int:recipe_id>', detail, name='detail'),
]  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)