from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    captions = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "user_image")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' '+ str(self.date.date())


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userImage = models.ImageField(upload_to = "Profiles", default = "default/default.png")
    bio = models.CharField(max_length=100, blank = True)
    connection = models.CharField(max_length = 100, blank=True)
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default=0)


    def __str__(self):
        return str(self.user)