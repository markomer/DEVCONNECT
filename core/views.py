from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post



class Home(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        liked_by = [[i.liker for i in x.postlikes.all()] for x in posts]
        context['posts'] = zip(posts, liked_by)

        return context
