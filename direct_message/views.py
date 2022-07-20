import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import DirectMessage
from django.db.models import Count
from django.contrib.auth.models import User
from django.db.models import Q


def message_page(request, pk = None):
    context = dict()
    if request.method == 'GET':
        if pk:
            user_picked = User.objects.get(pk = pk)
            context['convo_user'] = user_picked
            convo_yours = DirectMessage.objects.filter(sender = request.user, sent_to = user_picked)
            convo_theirs = DirectMessage.objects.filter(sender = user_picked, sent_to = request.user)
            context['convo'] = [(x , 'yours') if x.sender == request.user else (x, 'theirs') for x in convo_yours.union(convo_theirs).order_by('pk')]
            qs = DirectMessage.objects.filter(sender = user_picked, read = False)
            qs.update(read = True)
            context['new_message'] = True
    user = request.user
    unread_messages = DirectMessage.objects.filter(sent_to = user, read = False).values('sender').annotate(dcount=Count('sender'))
    users = [User.objects.get(pk = x['sender']) for x in unread_messages]
    context['unread_messages'] = zip(unread_messages, users)
    first_convo_list = DirectMessage.objects.filter(Q(sender = user) | Q(sent_to = user))
    convo_list = list()
    for x in first_convo_list:
        if x.sender == user:
            if x.sent_to not in convo_list:
                convo_list.append(x.sent_to)
        else:
            if x.sender not in convo_list:
                convo_list.append(x.sender)
    context['convo_list'] = convo_list
    context['user_list'] = User.objects.all()

    return render(request, 'direct_message/messages.html', context=context)



def new_message(request):
    DirectMessage.objects.create(message = request.POST['message'], sender = request.user, sent_to = User.objects.get(pk = request.POST['user']))
    user_picked = User.objects.get(pk = request.POST['user'])
    return redirect('messages', user_picked.pk)


def get_notified(request):
    user = request.user
    unread_messages = DirectMessage.objects.filter(sent_to = user, read = False)
    response_data = {}
    response_data['notifications'] = len(unread_messages)
    return HttpResponse(
                json.dumps(response_data),
                content_type='application.json'
            )

