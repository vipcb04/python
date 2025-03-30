from django.shortcuts import render
from .models import Artist, Song, Playlist

def home(request):
    artists = Artist.objects.all()
    songs = Song.objects.all().order_by('-created_at')[:10]  # 10 bài hát mới nhất
    return render(request, 'music_app/home.html', {
        'artists': artists,
        'songs': songs
    })

def artist_detail(request, pk):
    artist = Artist.objects.get(pk=pk)
    songs = artist.songs.all()
    
    return render(request, 'music_app/artist_detail.html', {
        'artist': artist,
        'songs': songs
    })

def song_detail(request, pk):
    song = Song.objects.get(pk=pk)
    return render(request, 'music_app/song_detail.html', {
        'song': song
    })