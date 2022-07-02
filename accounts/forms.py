
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from accounts.models import PROFESSION_CHOICES

class SignUpForm(UserCreationForm):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
  first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  prof = forms.CharField(max_length=15, widget=forms.Select(attrs={'class':'form-control'}))

  #  !!!! TRY forms.Select  ABOVE ^^^  !!!!


  #prof = forms.CharField(max_length=15, choices=PROFESSION_CHOICES, default='green')

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'prof', 'email', 'password1', 'password2' )

  #class Meta:
  #  model = ProfModel
  #  fields = ['prof']

  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'

#class ProfModelForm(UserCreationForm):
#    class Meta:
#        model = ProfModel
#        fields = ['prof']