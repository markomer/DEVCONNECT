from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

#from accounts.models import SignUp
from .forms import SignUpForm 
#ProfModelForm

from django.urls import reverse_lazy


class SignUpView(generic.CreateView):
  form_class = SignUpForm
  template_name = 'registration/signup.html'
  success_url = reverse_lazy('login')


#class CreateProfModelView(generic.CreateView):
#  model = ProfModel
#  form_class = ProfModelForm
#  template_name = 'registration/signup.html'
#  success_url = 'pages/home_in.html'