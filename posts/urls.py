from django.urls import path
from .views import (
  PostListView, PostCreateView,
  PostDetailView, PostUpdateView,
  PostDeleteView,
)
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
  path('', PostListView.as_view(), name='post_list'),
  path('new/', PostCreateView.as_view(), name='post_new'),
  path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
  path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
  path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
  path('create-like/<pk>', views.create_like_view, name = 'create_like'),
  path('create-comment/<pk>', views.create_comment_view, name = 'create_comment'),
  path('search_post_cats', views.search_post_cats, name = 'search_post_cats'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




