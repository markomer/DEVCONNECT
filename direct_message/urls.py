from django.urls import path
from . import views

urlpatterns = [
  path('', views.message_page, name='messages'),
  path('<int:pk>', views.message_page, name='messages'),
  path('new_message', views.new_message, name='new_message'),
]