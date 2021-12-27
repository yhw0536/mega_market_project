from django.shortcuts import redirect
from django.urls import path, include

from . import views

urlpatterns = [
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('signout/', views.signout),

]
