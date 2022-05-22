from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

USER = get_user_model()

# Create your models here.

class Profile(models.Model):
    user          = models.ForeignKey(to=USER, on_delete=models.CASCADE)
    id_user       = models.IntegerField()
    bio           = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to = 'profile_images', default = 'default-user-img.png')
    location      = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user        = models.CharField(max_length=100)
    image       = models.ImageField(upload_to = 'post')
    caption     = models.TextField()
    created_at  = models.DateField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id  = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowCount(models.Model):
    follower = models.CharField(max_length=100)
    user     = models.CharField(max_length=100)

    def __str__(self):
        return self.user