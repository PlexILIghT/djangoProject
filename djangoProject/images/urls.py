from django.urls import path

from images import views

urlpatterns = [
    path('image', views.show_image),
]
