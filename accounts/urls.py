from django.urls import path, include
from .views import SignUpView, UserEditView
#, LogoutView 


urlpatterns = [
  path('signup/', SignUpView.as_view(), name='signup'),
  path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
  #path('logout/', LogoutView.as_view(), name='logout'), 
]