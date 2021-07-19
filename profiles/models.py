from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    location = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='uploads/profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

