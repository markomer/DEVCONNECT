from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'author':forms.HiddenInput(attrs={'class' : 'form-control' }),
            'body' : forms.Textarea(attrs={'class' : 'form-control' }),
        }