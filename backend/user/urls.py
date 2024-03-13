from django.urls import path
from .views import UserRegistrationView,UserLoginView,AdminLoginView,UserListAPIView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('admin_login/', AdminLoginView.as_view(), name='admin_login'),
    path('user_list/', UserListAPIView.as_view(), name='user_list'),
    
]