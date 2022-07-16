from django.urls import path
from .views import HomePageView, AboutPageView, HomeInPageView, HomeLogoutPageView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('about/', AboutPageView.as_view(), name='about'),
  path('home_in/', HomeInPageView.as_view(), name='home_in'),
  path('home_logout/', HomeLogoutPageView.as_view(), name='home_logout')
]