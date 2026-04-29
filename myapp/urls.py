from django.http import HttpResponse
from django.urls import path
from myapp.views import signup, profile_setup, home, add_friend, user_profile, generate_description
from django.shortcuts import render
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("success/", lambda r: render(r, "success.html"), name="profile_success"),
    path("profile-setup/", profile_setup, name="profile_setup"),

    path("password-reset/",
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name="password_reset"),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

    path("add_friend/<int:user_id>", add_friend, name="add_friend"),
    path("user_profile/<int:friend_id>", user_profile, name="user_profile"),

    path('generate_description/', generate_description, name='generate_description'),
]
