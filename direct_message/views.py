from django.shortcuts import redirect, render
from .models import DirectMessage
from django.db.models import Count
from django.contrib.auth.models import User


def message_page(request):
    if request.method == 'GET':
        user = request.user
        context = dict()
        unread_messages = DirectMessage.objects.filter(sent_to = user, read = False).values('sender').annotate(dcount=Count('sender'))
        users = [User.objects.get(pk = x['sender']) for x in unread_messages]
        context['unread_messages'] = zip(unread_messages, users)
        context['convo'] = None
        print(context['unread_messages'])
        return render(request, 'direct_message/messages.html', context=context)

