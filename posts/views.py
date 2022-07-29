import json
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.urls import reverse_lazy
from .models import Post, Like, Comment
from .forms import PostForm
from django.core.paginator import Paginator


class PostCreateView(LoginRequiredMixin, CreateView):
  template_name = 'posts/new.html'
  model = Post
  form_class = PostForm
  #fields = ['title', 'title_tag', 'body',]
  success_url = reverse_lazy('post_list')


  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
    

class PostListView(LoginRequiredMixin, ListView):
  template_name = 'posts/list.html'
  model = Post
  paginate_by = 3
  context_object_name = "posts"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['likers'] = [[i.liker for i in x.postlikes.all()] for x in Post.objects.all()]
    return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  template_name = 'posts/edit.html'
  model = Post
  form_class = PostForm
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

    
#========= Read Single-Post Detail =========
#======?????? Using this..??????======
class PostDetailView(DetailView):
  template_name = 'posts/detail.html'
  model = Post



#========= Search Posts thru two Categories =========

def search_post_cats(request):
  if request.method == "POST":
    searched = request.POST.get('searched')
    searchedAgain = request.POST.get('searchedAgain')
    profposts = Post.objects.filter(Q(prof_category__icontains=searched) & Q(dev_category__icontains=searchedAgain))
    return render(request, 'posts/search_post_cats.html', {'searched':searched, 'searchedAgain':searchedAgain, 'posts':profposts})
  else:
    return render(request, 'posts/search_post_cats.html', {})
    

#========= likes & comments - views =========

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
