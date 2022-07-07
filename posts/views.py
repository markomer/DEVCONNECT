from itertools import chain
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
  CreateView,
  UpdateView,
  DeleteView
)
from .models import Post, Like, Comment
from django.contrib.auth.mixins import (
  LoginRequiredMixin, UserPassesTestMixin)
from django.urls import reverse_lazy
from .forms import PostForm


   #def home(request):
   #  return render(request, 'home.html', {})

class PostListView(ListView):
  template_name = 'posts/list.html'
  model = Post

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    posts = Post.objects.all()
    liked_by = [[i.liker for i in x.postlikes.all()] for x in posts]
    context['posts'] = zip(posts, liked_by)
    return context


class PostDetailView(DetailView):
  template_name = 'posts/detail.html'
  model = Post
  success_url = reverse_lazy('post_list') 
  

class PostCreateView(LoginRequiredMixin, CreateView):
  template_name = 'posts/new.html'
  model = Post
  form_class = PostForm
  #fields = ['title', 'title_tag', 'body',]
  success_url = reverse_lazy('post_list')

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  template_name = 'posts/edit.html'
  model = Post
  form_class = PostForm
  #fields = ['title', 'title_tag', 'body']
  success_url = reverse_lazy('post_list')

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  template_name = 'posts/delete.html'
  model = Post
  success_url = reverse_lazy('post_list')

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user


def create_like_view(request, pk):
    try:
        response_data = {}
        post = Post.objects.get(pk = pk)
        if request.user in [x.liker for x in post.postlikes.all()]:
            Like.objects.get(liker = request.user, post = post).delete()
            response_data['liked'] = True
        else:
            Like.objects.create(liker = request.user, post = post)
            response_data['liked'] = False
        response_data['num_likes'] = len(post.postlikes.all())
        return HttpResponse(
                    json.dumps(response_data),
                    content_type='application.json'
                )
    except Exception as e:
        print(f'create like error: {e}')

def create_comment_view(request, pk):
    try:
        response_data = {}
        post = Post.objects.get(pk = pk)
        Comment.objects.create(post = post,commenter = request.user, comment_body = request.POST['comment_body'])
        response_data['num_likes'] = len(post.postcomments.all())
        return HttpResponse(
                    json.dumps(response_data),
                    content_type='application.json'
                )
    except Exception as e:
        print(f'create like error: {e}')
