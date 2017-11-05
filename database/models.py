from django.db import models

# Create your models here.

class Post(models.Model):
    imgURL = models.CharField(max_length=400)
    caption = models.TextField(default="")
    postedBy = models.CharField(max_length=50)

class Like(models.Model):
    likedBy = models.CharField(max_length=50)
    post = models.ForeignKey(Post, related_name="likes")