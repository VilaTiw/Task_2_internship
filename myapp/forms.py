from django import forms
from django.contrib.auth.forms import UserCreationForm
from myapp.models import User, UserProfile

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("age", "location", "interests", "fav_color")