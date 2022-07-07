from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# from ckeditor.fields import RichTextField

class Category(models.Model):
  name = models.CharField(max_length=255, default="Title Goes Here")

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    # return reverse('article-detail', args=(str...))
    return reverse('post_list')



class Post(models.Model):
  title = models.CharField(max_length=256)
  # below--v CC Vid#3
  title_tag = models.CharField(max_length=255)
  header_image = models.ImageField(null=True, blank=True, upload_to="images/")
  author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE
  )
  body = models.TextField(max_length=400)
  created_on = models.DateTimeField(
    auto_now_add=True
  )
  category = models.CharField(max_length=255, default='all')

  #def total_likes(self):
  #  return self.likes.count()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post_detail', args=[self,id])

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