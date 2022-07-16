from django.urls import path
from .views import (
  PostListView, PostCreateView,
  PostDetailView, PostUpdateView,
  PostDeleteView,
)
from . import views

urlpatterns = [
  path('', PostListView.as_view(), name='post_list'),
  path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
  path('new/', PostCreateView.as_view(), name='post_new'),
  path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
  path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
  path('create-like/<pk>', views.create_like_view, name = 'create_like'),
  path('create-comment/<pk>', views.create_comment_view, name = 'create_comment'),
  path('search_post_cats', views.search_post_cats, name = 'search_post_cats'),
  #path('search_cat_lists/', views.search_cat_lists(), name='post_search_cat_lists'),
  #path('search_post_cats/', SearchResultsView.as_view(), name = 'search_post_cats'),
  #path('', PostListView.as_view(), name='home'),
  #path('user/update/', PostUpdateView.as_view(), name='user_update'),
]




