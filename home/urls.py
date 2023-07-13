from django.urls import path

from . import views

urlpatterns = [
    path('home', views.test),
    path('user/signup', views.handleSignup),
    path('user/login', views.handleLogin)
]
