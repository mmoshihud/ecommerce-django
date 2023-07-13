from django.urls import path

from . import views

urlpatterns = [
    path('home', views.test),
    path('user/signup', views.handleSignup),
    path('user/login', views.handleLogin),
    path('get-csrf-token', views.get_csrf_token)
]
