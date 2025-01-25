from django.urls import path
from .views import register_view, login_view, profile_view, delete_user_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('delete/', delete_user_view, name='delete_user'),
    path('logout/', logout_view, name="logout_view")
]
