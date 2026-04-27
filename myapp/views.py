from django.shortcuts import render, redirect
from django.contrib.auth import login
from myapp.forms import SignUpForm, UserProfileForm
from myapp.tasks import send_welcome_email

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            send_welcome_email.delay(user.email, user.username)
            login(request, user)
            return redirect("profile_success")
    else:
        user_form = SignUpForm()
        profile_form = UserProfileForm()

    return render(request, "signup.html", {"user_form": user_form, "profile_form": profile_form})