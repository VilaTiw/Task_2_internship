from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import JsonResponse
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from myapp.forms import SignUpForm, UserProfileForm
from myapp.tasks import send_welcome_email
from myapp.ai_services import generate_user_description
import time

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("profile_setup")
    else:
        user_form = SignUpForm()

    return render(request, "signup.html", {"user_form": user_form})

@login_required
def profile_setup(request):
    profile = request.user.profile

    if all([profile.age, profile.location, profile.interests, profile.fav_color]):
        return redirect("profile_success")

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            send_welcome_email.delay(profile.user.email, profile.user.username)
            return redirect("profile_success")
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "profile_setup.html", {"form": form})

@login_required
def generate_description(request):
    user_id = request.user.id
    cache_key = f"ai_throttle_{user_id}"

    last_request_time = cache.get(cache_key)

    if last_request_time:
        wait_time = int(1200 - (time.time() - last_request_time))
        if wait_time > 0:
            wait_min = wait_time // 60
            wait_sec = wait_time % 60
            return JsonResponse({"error": f"Too many requests! Try again in {wait_min} minutes and {wait_sec} seconds."}, status=429)

    profile = request.user.profile

    if not all([profile.age, profile.location, profile.interests, profile.fav_color]):
        return JsonResponse({"error": "First, fill out all the profile fields!"}, status=400)

    user_data = {
        "name": profile.user.username,
        "age": profile.age,
        "location": profile.location,
        "interests": profile.interests,
    }

    try:
        ai_description = generate_user_description(user_data)
        profile.description = ai_description
        profile.save()

        cache.set(cache_key, time.time(), 1200)

        return JsonResponse({"description": ai_description}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)