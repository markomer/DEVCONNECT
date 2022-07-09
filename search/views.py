from intertools import chain
from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Post

class SearchView(ListView):
  template_name = 'posts/search_posts.html'
  paginate_by = 20
  count = 0

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['count'] = self.count or 0
    context['query'] = self.request.GET.get('q')
    return context

  def get_queryset(self):
    request = self.request
    query = request.GET.get('q', None)

    if query is not None:
      post_results = Post.objects.search(query=query)
      post_results = Post.objects.search(query=query)

      queryset_chain = chain(post_results, post_results)
      qs = sorted(queryset_chain,
        key=lambda instance: instance.pk,
        reverse=True)
      self.count = len(qs)
      return qs

    return Post.objects.none()



  success_url = reverse_lazy('post_list')
