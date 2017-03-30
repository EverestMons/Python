from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.db.models import count
# Create your views here.
def index (request):
    context = {
    'playlists': Playlist.objects.all(),
    'title': 'The World\'s Greatest Playlist Manager'

    }
    return render(request, 'playlistManager/index.html', context)

def create_playlist(request):
    playlist_name = request.POST['playlist_name']
    try:
        Playlist.objects.create(name = playlist_name)
    except:
        messages.error(request,'Playlist must have a unique name.')
    return redirect('pytunes:index')

def add_song(request, playlist_id):
    if request == 'POST':
        song_name = request.POST['song_name']
        try:
            Song.objects.create(name = song_name)
        except:
            messages.error(request, 'Song must havea a unique name.')
        return redirect(reverse('pytunes:add_song', kwargs = {'playlist_id=playlist_id'})
    context = {
    'playlist': Playlist.objects.get(id=playlist_id),
    'songs': Song.objects.filter(playlist_id = playlist_id)
    }

    return render(request, 'playlistManager/songs.html', context)
