
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
#from accounts.models import PROFESSION_CHOICES


#=========== SignUp Form Items ============================
#===?????? ProfCat & DevCat Needed..??????=================

PROF_CHOICES = (
  ('professional', 'Professional'),
  ('student', 'Student'),
  ('instructor', 'Instructor')
)

DEV_CHOICES = (
  ('frontend', 'Front End'),
  ('backend', 'Back End'),
  ('fullstack', 'Full Stack')
)

class SignUpForm(UserCreationForm):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
  first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  prof = forms.ChoiceField(label="Choose Profession Type", choices=(PROF_CHOICES), widget=forms.Select(attrs={'class':'form-control'}))

  dev = forms.ChoiceField(label="Choose Development Type", choices=(DEV_CHOICES), widget=forms.Select(attrs={'class':'form-control'}))

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'prof', 'dev', 'email', 'password1', 'password2' )

  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'


#=========== EditPofile Form Items ============================
#===?????? ProfCat & DevCat Needed..??????=================

class EditProfileForm(UserChangeForm):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
  first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
  is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
  is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
  date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

  prof = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

  prof = forms.ChoiceField(label="Choose Profession Type", choices=(PROF_CHOICES), widget=forms.Select(attrs={'class':'form-choice'}))

  dev = forms.ChoiceField(label="Choose Developer Type", choices=(DEV_CHOICES), widget=forms.Select(attrs={'class':'form-control'}))

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'prof', 'dev', 'email', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined') 

