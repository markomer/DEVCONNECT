from django.urls import path
from . import views

urlpatterns = [
  path('', views.message_page, name='messages'),
]