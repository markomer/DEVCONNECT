from . import views
from django.urls import path, include
from .views import CreatePostView, DeletePostView, UpdatePostView
from . import views

urlpatterns = [
    path('new_post', CreatePostView.as_view(), name = 'new_post'),
    path('delete_post/<pk>', DeletePostView.as_view(), name = 'delete_post'),
    path('update_post/<pk>', UpdatePostView.as_view(), name = 'update_post'),
    path('create-like/<pk>', views.create_like_view, name = 'create_like'),
]

