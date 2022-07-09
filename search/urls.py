from django.urls import path
from . import Views

urlpatterns = [
  path('', views.home, name="home"),
  path('search_posts/', views.search. name-'search-posts')
]