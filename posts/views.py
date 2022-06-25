import json
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import PostForm
import io

# =============================CREATE=============================

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/new_post.html'
    form_class = PostForm

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = User.objects.get(pk = self.request.user.pk)
        return initial

def create_like_view(request, pk):
    post = Post.objects.get(pk = pk)
    Like.objects.create(liker = request.user, post = post)
    response_data = {'num_likes': len(post.postlikes.all())}
    return HttpResponse(
                json.dumps(response_data),
                content_type='application.json'
            )


# =============================READ=============================


# =============================UPDATE=============================

class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/update_post.html'
    form_class = PostForm

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = User.objects.get(pk = self.request.user.pk)
        return initial


# =============================DELETE=============================

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'

    def get_success_url(self):
        return reverse_lazy('home')