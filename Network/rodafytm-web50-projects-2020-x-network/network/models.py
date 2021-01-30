from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, default=None)
    content = models.CharField(max_length=140, default=None)
    timestamp = models.DateTimeField(default=datetime.now())
    liked = models.ManyToManyField('User', default=None, blank=True, related_name='post_likes')

    @property
    def num_likes(self):
        return self.liked.all().count()

class Like(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, default=None)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default=None)

class Profile(models.Model):
    target = models.ForeignKey('User', on_delete=models.CASCADE, related_name='folowers', default=None)
    follower = models.ForeignKey('User', on_delete=models.CASCADE, related_name='targets', default=None)

def __str__(self):
        return str(self.post)
