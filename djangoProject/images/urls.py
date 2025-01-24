from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import show_image, like_image

urlpatterns = [
    path('', show_image, name='show_images'),
    path('like/<int:image_id>/', like_image, name='like_image'),
]
