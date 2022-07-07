from itertools import chain
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
  CreateView,
  UpdateView,
  DeleteView)
from .models import Post
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.urls import reverse_lazy
from .forms import PostForm


   #def home(request):
   #  return render(request, 'home.html', {})

class PostListView(ListView):
  template_name = 'posts/list.html'
  model = Post


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

   
