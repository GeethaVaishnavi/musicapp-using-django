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
