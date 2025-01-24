from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from misc import views

urlpatterns = [
    path("", views.homepage_view, name="homepage"),
    path("task3", views.task3, name="task3"),
    path("redirected", views.redirected, name="redirected"),
]