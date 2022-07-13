from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


#============== Post Creation - model ==================

class Post(models.Model):
  title = models.CharField(max_length=256)
  # below--v CC Vid#3 - title_tag & header_image
  title_tag = models.CharField(max_length=255)
  #header_image = models.ImageField(null=True, blank=True, upload_to="images/")
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  body = models.TextField(max_length=400)
  created_on = models.DateTimeField(auto_now_add=True)
  category = models.CharField(max_length=255, default='all')

  #objects = PostManager()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post_detail', args=[self,id])


#============== Post Categories - select choices ============

class Category(models.Model):
  name = models.CharField(max_length=255, default="Cat Goes here")

  def __str__(self):
    #return self.name
    return self.name

  def get_absolute_url(self):
    # return reverse('article-detail', args=(str...))
    return reverse('post_list')


#=============== Post Likes & Comments ======================

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


PROFESSIONAL_CATEGORIES = [
  ('all', 'all'),
  ('professional-all', 'professional-all'),
  ('professional-frontend', 'professional-frontend'),
  ('professional-backend', 'professional-backend'),
  ('professional-fullstack', 'professional-fullstack'),
  ('hobbiest-all', 'hobbiest-all'),
  ('hobbiest-frontend', 'hobbiest-frontend'),
  ('hobbiest-backend', 'hobbiest-backend'),
  ('hobbiest-fullstack', 'hobbiest-fullstack'),
  ('instructor-all', 'instructor-all'),
  ('instructor-frontend', 'instructor-frontend'),
  ('instructor-backend', 'instructor-backend'),
  ('instructor-fullstack', 'instructor-fullstack'),
]

DEVELOPMENT_CATEGORIES = [
  ('all', 'all'),
  ('professional-all', 'professional-all'),
  ('professional-frontend', 'professional-frontend'),
  ('professional-backend', 'professional-backend'),
  ('professional-fullstack', 'professional-fullstack'),
  ('hobbiest-all', 'hobbiest-all'),
  ('hobbiest-frontend', 'hobbiest-frontend'),
  ('hobbiest-backend', 'hobbiest-backend'),
  ('hobbiest-fullstack', 'hobbiest-fullstack'),
  ('instructor-all', 'instructor-all'),
  ('instructor-frontend', 'instructor-frontend'),
  ('instructor-backend', 'instructor-backend'),
  ('instructor-fullstack', 'instructor-fullstack'),
]



#class CatsCombine(models.Model):
#    prof_cats = models.CharField(max_length=128, choices=PROFESSIONAL_CATEGORIES, default='all_professions_cats')
#    dev_cats = models.CharField(max_length=128, choices=DEVELOPMENT_CATEGORIES, default='all_development_cats')

#================ Posts Query Filter - vrsn 1 ==================

# from ckeditor.fields import RichTextField
#
#class PostQuerySet(models.QuerySet):
#  def search(self, query=None):
#    qs = self
#    if query is not None:
#      and_lookup = (Q(category__icontains=query) |
#                    Q(title_tag__icontains=query)
#                  )
#      qs = qs.filter(and_lookup).distinct() 
#    return qs
##
#class PostManager(models.Manager):
#  def get_queryset(self):
#    return PostQuerySet(self.model, using=self._db)
##
#  def search(self, query=None):
#    return self.get_queryset().search(query=query)
###########
# PostManager above is what is used with PostQuerySet()
# remodelled from below version - standing alone
###########
#class PostManager(models.Manager):
#  def search(self, query=None):
#    qs = self.get_queryset()
#    if query is not None:
#      and_lookup = (Q(category__icontains=query) |
#                    Q(title_tag__icontains=query)
#                  )
#      qs = qs.filter(and_lookup).distinct() 
#    return qs
