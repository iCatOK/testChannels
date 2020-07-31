from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.
from django.utils.safestring import mark_safe
import json
from .models import Chat


def index(request):
    return render(request, 'chat/index.html')

@login_required
def lobby(request):
    return render(request, 'chat/lobby.html', {
        'username': mark_safe(json.dumps(request.user.username)),
    })

@login_required
def room(request, room_id):
    chat = Chat.objects.get(id=room_id)
    partner = chat.users.all()[0].username
    if chat.users.all()[0].username == request.user.username:
        partner = chat.users.all()[1].username
    return render(request, 'chat/room.html', {
        'room_id': room_id,
        'username': mark_safe(json.dumps(request.user.username)),
        'partner': partner
    })



