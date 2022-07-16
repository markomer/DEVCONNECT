#from socket import fromshare
#from django import fromshare
from django import forms
from .models import Post, Category



#########

# THIS FORMS FILE IS NOT YET IN USE
# REFER TO POSTS/MODELS.PY

#choices = [
#  ('all', 'all'),
#  ('professional-all', 'professional-all'),
#  ('professional-all', 'professional-all'),
#  ('professional-all', 'professional-all'),
#  ]

#########

#choices = Category.objects.all().values_list('name','name')

prof_choices = [
  #('AlL', 'ALL'),
  ('Professional', 'Professional'),
  #('professional-frontend', 'professional-frontend'),
  #('professional-backend', 'professional-backend'),
  #('professional-fullstack', 'professional-fullstack'),
  ('Hobbiest', 'Hobbiest'),
  #('hobbiest-frontend', 'hobbiest-frontend'),
  #('hobbiest-backend', 'hobbiest-backend'),
  #('hobbiest-fullstack', 'hobbiest-fullstack'),
  ('Instructor', 'Instructor'),
  #('instructor-frontend', 'instructor-frontend'),
  #('instructor-backend', 'instructor-backend'),
  #('instructor-fullstack', 'instructor-fullstack'),
]

dev_choices = [
  ('All', 'All'),
  ('Frontencd', 'Frontend'),
  ('Backend', 'Backend'),
  ('Fullstack', 'Fullstack'),
  #('professional-all', 'professional-all'),
  #('professional-frontend', 'professional-frontend'),
  #('professional-backend', 'professional-backend'),
  #('professional-fullstack', 'professional-fullstack'),
  #('hobbiest-all', 'hobbiest-all'),
  #('hobbiest-frontend', 'hobbiest-frontend'),
  #('hobbiest-backend', 'hobbiest-backend'),
  #('hobbiest-fullstack', 'hobbiest-fullstack'),
  #('instructor-all', 'instructor-all'),
  #('instructor-frontend', 'instructor-frontend'),
  #('instructor-backend', 'instructor-backend'),
  #('instructor-fullstack', 'instructor-fullstack'),
]

#for item in choices:
#  choices.append(item)


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'prof_category', 'dev_category', 'body',)
    #fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', #'header_image')

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter Title here'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter Taggy here - optional'}),
      'prof_category': forms.Select(choices=prof_choices, attrs={'class': 'form-control'}),
      #'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'?'}),
      #'author': forms.Select(attrs={'class': 'form-control'}),
      'dev_category': forms.Select(choices=dev_choices, attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      #'snippet': forms.Textarea(attrs={'class': 'form-control'}),
    }


class SearchForm(forms.Form):
  q = forms.CharField(label='Search', max_length=50)



