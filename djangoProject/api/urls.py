from django.urls import path
from .views import user_list, user_detail, user_create, user_update, user_delete

urlpatterns = [   
    path('user/', user_list, name='user_list'),
    path('user/<int:user_id>/', user_detail, name='user_detail'),
    path('user/create/', user_create, name='user_create'),
    path('user/<int:user_id>/update/', user_update, name='user_update'),
    path('user/<int:user_id>/delete/', user_delete, name='user_delete'),
]