from django.urls import path

from . import views

urlpatterns = [
    path('user/signup', views.handleSignup),
    path('user/login', views.handleLogin)
]
