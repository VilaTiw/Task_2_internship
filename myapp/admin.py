from django.contrib import admin

from myapp.models import User, UserProfile, UserFriends

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserFriends)