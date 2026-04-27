from django.http import HttpResponse
from django.urls import path
from myapp.views import signup
from django.shortcuts import render

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("success", lambda r: render(r, "success.html"), name="profile_success"),
]