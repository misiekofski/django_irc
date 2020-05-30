from django.shortcuts import render


def index(request):
    return render(request, 'chatex/index.html')


def room(request, room_name):
    return render(request, 'chatex/room.html', {
        'room_name': room_name
    })