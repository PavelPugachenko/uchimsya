from django.contrib.auth import login
from django.urls import path
from .views import RegisterView
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'users'

urlpatterns = [
    path ('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path ('logout/', LogoutView.as_view(), name='logout'),
]
