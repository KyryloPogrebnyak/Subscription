from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
 
    path("", views.home, name=""),
    path("register/", views.register, name="register"),
    path("login_view/", views.login_view, name="login_view"),
    path("user_logout/", views.user_logout, name="user_logout"),
]