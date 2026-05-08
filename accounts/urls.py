from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('user/register/', views.register_user_view, name='register'),
    path('user/login/', views.login_user_view, name='login'),
    path('user/logout/', views.logout_user_view, name='logout'),
    path('user/', views.user_view, name='user'),
]
