from django.urls import path
from .views import HomePageView, AboutPageView, HomeInPageView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('about/', AboutPageView.as_view(), name='about'),
  path('home_in/', HomeInPageView.as_view(), name='home_in')
]