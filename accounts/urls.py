from django.urls import path

from .views import SignUpView 
#CreateProfModelView


urlpatterns = [
  path('signup/', SignUpView.as_view(), name='signup'),
  #path('signup/', CreateProfModelView.as_view(), name='signup')
]