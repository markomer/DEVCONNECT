#from socket import fromshare
#from django import fromshare
from django import forms
from .models import Post, Category



#########

# THIS FORMS FILE IS NOT YET IN USE
# REFER TO POSTS/MODELS.PY

#########


#choices = [
#  ('all', 'all'),
#  ('professional-all', 'professional-all'),
#  ('professional-all', 'professional-all'),
#  ('professional-all', 'professional-all'),
#  ]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
  choice_list.append(item)


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'category', 'body',)
    #fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', #'header_image')

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter Title here'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter Tag here - optional'}),
      'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
      #'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'?'}),
      #'author': forms.Select(attrs={'class': 'form-control'}),
      #'category': forms.Select(choices=choices....'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      #'snippet': forms.Textarea(attrs={'class': 'form-control'}),
    }

