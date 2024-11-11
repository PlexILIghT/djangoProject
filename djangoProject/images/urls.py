from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from images import views

urlpatterns = [
    path('', views.show_image),
]
