from django.db import models
from django.urls import reverse

class DirectMessage(models.Model):
    message = models.TextField(max_length=256)
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='sender')
    sent_to = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='sendtos')
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.sender.username


