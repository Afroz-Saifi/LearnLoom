from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('register', views.register_user, name='register-user'),
    path('login', views.user_login, name='user-login'),
]
