from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('users/', views.users_view, name='users'),
    path('new_user/', views.new_user_view, name='new_user'),
    path('users/<int:id>/', views.user_detail_view, name='user_detail'),
]