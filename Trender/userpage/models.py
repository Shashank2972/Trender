from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    captions = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "user_image" , blank=True)
    date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return (self.user) + ' '+ str(date.date())
