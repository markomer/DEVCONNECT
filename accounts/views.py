from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import CreateView
from .forms import SignUpForm

#from accounts.models import SignUp
from .forms import SignUpForm, EditProfileForm 
#ProfModelForm

from django.urls import reverse_lazy


class SignUpView(generic.CreateView):
  form_class = SignUpForm
  template_name = 'registration/signup.html'
  success_url = reverse_lazy('login')


def login_user(request):
  if request.method =="POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username, password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.success(request, ("There Was An Error"))
      return redirect('login')

  else:
    return render(request, 'authenticate/login.html',)


def register_user(request):
  if request.method =="POST":
    form = SignUpForm(request.Post)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['user']
      password = form.cleaned_data['password']
      user = authenticate(username=username)
      login(request, user)
      messagees.success(request, ("Register"))
      return redirect('home')
  else:
    form = SignUpForm()

  return render (request, 'authenticate/signup.html')
    

class UserEditView(generic.UpdateView):
  form_class = EditProfileForm
  template_name = 'registration/edit_profile.html'
  success_url = reverse_lazy('home_in')

  def get_object(self):
    return self.request.user


#class CreateProfModelView(generic.CreateView):
#  model = ProfModel
#  form_class = ProfModelForm
#  template_name = 'registration/signup.html'
#  success_url = 'pages/home_in.html'