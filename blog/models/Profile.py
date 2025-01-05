from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    ciudad = models.TextField(default='ciudad')

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        first_name = self.user.first_name or ''
        last_name = self.user.last_name or ''
        return f"{first_name} {last_name}".strip()

