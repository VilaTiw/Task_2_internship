from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   email = models.EmailField(max_length=255, unique=True)

   def __str__(self):
       return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    interests = models.TextField(max_length=255)
    fav_color = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"Profile of {self.user.username}"

class UserFriends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends_starter')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends_target')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'friend')

    def __str__(self):
        return f"User {self.user.username} is friends of {self.friend.username}"