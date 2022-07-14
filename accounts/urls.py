from django.urls import path, include

from .views import SignUpView, UserEditView, LogoutPageView 
#CreateProfModelView


urlpatterns = [
  path('signup/', SignUpView.as_view(), name='signup'),
  path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
  #path('logout/', LogoutPageView.as_view(), name='logout'),

  #path('signup/', CreateProfModelView.as_view(), name='signup')
]