from django.urls import path

from .views import SignUpView, UserEditView 
#CreateProfModelView


urlpatterns = [
  path('signup/', SignUpView.as_view(), name='signup'),
  path('edit_profile/', UserEditView.as_view(), name='edit_profile'),

  #path('signup/', CreateProfModelView.as_view(), name='signup')
]