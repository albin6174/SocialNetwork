from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    uploaded_date=models.DateTimeField(auto_now_add=True)
    upvote=models.ManyToManyField(User,related_name="post")

    def __str__(self):
        return self.title
    
    @property
    def likes_count(self):
        return self.upvote.all().count()
    
    @property
    def post_comments(self):
        return Comments.objects.filter(post=self)

class UserProfile(models.Model):
    profile_pic=models.ImageField(upload_to="images",null=True)
    bio=models.CharField(max_length=500)
    time_line_pic=models.ImageField(upload_to="images",null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")   


class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=300)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,null=True)
    upvote=models.ManyToManyField(User,related_name="Liked")

    def __str__(self):
        return self.post
