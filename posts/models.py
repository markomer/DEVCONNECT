from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


#========= Post Creation - model =========

class Post(models.Model):
    title = models.CharField(max_length=256)
    # below--v CC Vid#3 - title_tag & header_image
    title_tag = models.CharField(max_length=255)
    #header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(max_length=999)
    created_on = models.DateTimeField(auto_now_add=True)
    prof_category = models.CharField(max_length=255, default='all')
    dev_category = models.CharField(max_length=255, default='all')
  
    def liker(self):
        return [x.liker for x in self.postlikes.all()]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self,id])


#========= Post Likes & Comments =========

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postlikes')



    class Meta:
        db_table = 'like'
        app_label = 'posts'

    def __str__(self) -> str:
        return f'{self.liker}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postcomments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    date_commented = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    comment_body = models.TextField(max_length=2000, null=True, blank=True)

    class Meta:
        db_table = 'comment'
        app_label = 'posts'

    def __str__(self) -> str:
        return f'{self.commenter}'


