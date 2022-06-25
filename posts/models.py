from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    date_commented = models.DateField(auto_now_add=True, null=True, blank=True)
    comment_body = models.TextField(max_length=2000, null=True, blank=True)

    class Meta:
        db_table = 'comment'
        app_label = 'posts'

    def __str__(self) -> str:
        return f'{self.commenter}'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField(max_length=2000, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'post'
        app_label = 'posts'

    def __str__(self) -> str:
        return f"{self.author}'s post"

    def get_absolute_url(self):
        return reverse('home')


class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postlikes')

    class Meta:
        db_table = 'like'
        app_label = 'posts'

    def __str__(self) -> str:
        return f'{self.liker}'
