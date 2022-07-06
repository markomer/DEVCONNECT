
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
#from accounts.models import PROFESSION_CHOICES



PROF_CHOICES = (
  ('professional', 'Professional'),
  ('hobbiest', 'Hobbiest'),
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
  prof = forms.ChoiceField(label="Choose Profession Type", choices=(PROF_CHOICES), widget=forms.Select(attrs={'class':'form-choice'}))

  dev = forms.ChoiceField(label="Choose Developer Type", choices=(DEV_CHOICES), widget=forms.Select(attrs={'class':'form-control'}))

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'prof', 'dev', 'email', 'password1', 'password2' )

  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'


  # 20220705 - trying below code for sign up "memory"...???...
  #def post(self, request, *args, **kwargs):
  #  form = SignUpForm(request.POST)
  #  if form.is_valid():
  #    form.save()
  #    email = form.cleaned_data.get('email')
  #    raw_password = form.cleaned_data.get('password1')
  #    user = authenticate(request, username=email, passwrod=raw_password)
  #    login(request, user)
  #    return redirect('home')
  #  return render(request, self.template_name, {'form': form})
  #
  #def get(self, request, *args, **kwargs):
  #  return render(request, self.template_name)




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


  prof = forms.ChoiceField(label="Choose Profession Type", choices=(PROF_CHOICES), widget=forms.Select(attrs={'class':'form-choice'}))

  dev = forms.ChoiceField(label="Choose Developer Type", choices=(DEV_CHOICES), widget=forms.Select(attrs={'class':'form-control'}))

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'prof', 'dev', 'email', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined') 


 

  #def save(self, commit=True):
  #  # Save the provided password in hashed format
  #  user = super().save(commit=False)
  #  user.set_password(self.cleaned_data["password"])
  #  user.user_type = 1
  #  if commit:
  #    user.save()
#
#      # Extract your profile data from self.cleaned_data
#      profile_data = self.cleaned_data
#
#      profile_form = EditProfileForm(profile_data)
#
#      profile_form.save()
#    return user

  
    
