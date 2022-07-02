from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
  title = models.CharField(max_length=256)

  author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE
  )

  body = models.TextField(max_length=400)

  created_on = models.DateTimeField(
    auto_now_add=True
  )

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post_detail', args=[self,id])

# Create your models here.
