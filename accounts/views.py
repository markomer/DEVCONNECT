from django.shortcuts import render, redirect
from django.views import generic
from .forms import SignUpForm, EditProfileForm 
from django.urls import reverse_lazy
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.views.generic.edit import CreateView
#from django.views.generic import TemplateView


#=========== User SignUp  =================

class SignUpView(generic.CreateView):
  form_class = SignUpForm
  template_name = 'registration/signup.html'
  success_url = reverse_lazy('login')

#=========== Edit User Profile  =================

class UserEditView(generic.UpdateView):
  form_class = EditProfileForm
  template_name = 'registration/edit_profile.html'
  success_url = reverse_lazy('home_in')

  def get_object(self):
    return self.request.user

