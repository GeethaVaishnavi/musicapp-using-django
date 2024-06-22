from django.shortcuts import render, get_object_or_404
from .models import Artist, Album, Song

def index(request):
    artists = Artist.objects.all()
    albums = Album.objects.all()
    songs = Song.objects.all()
    return render(request, 'music/index.html', {'artists': artists, 'albums': albums, 'songs': songs})

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'music/artist_detail.html', {'artist': artist})

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/album_detail.html', {'album': album})
# views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Song

def download_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    file_path = song.file.path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='audio/mpeg')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(file_path))
        return response
# views.py

from django.shortcuts import render
from .models import Album

def dashboard(request):
    albums = Album.objects.all()
    return render(request, 'music/dashboard.html', {'albums': albums})
