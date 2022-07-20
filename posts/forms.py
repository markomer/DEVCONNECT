#from socket import fromshare
#from django import fromshare
from django import forms
from .models import Post


#########

prof_choices = [
  ('Professional', 'Professional'),
  ('Student', 'Student'),
  ('Instructor', 'Instructor'),
]

dev_choices = [
  ('General-All', 'General-All'),
  ('Frontend', 'Frontend'),
  ('Backend', 'Backend'),
  ('Fullstack', 'Fullstack'),
]

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'prof_category', 'dev_category', 'body',)
    #fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter Title here'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter Taggy here - optional'}),
      'prof_category': forms.Select(choices=prof_choices, attrs={'class': 'form-control'}),
      'dev_category': forms.Select(choices=dev_choices, attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      #'snippet': forms.Textarea(attrs={'class': 'form-control'}),
    }

