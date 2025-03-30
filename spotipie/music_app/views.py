from django.shortcuts import render,redirect, get_object_or_404
from .models import Artist, Song, Playlist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import ArtistForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def home(request):
    artists = Artist.objects.all()
    songs = Song.objects.all().order_by('-created_at')[:10]  
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
def create_form(request):
    
    return render(request, 'music_app/song_form.html')
@login_required
def add_song(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        audio_file = request.FILES.get('audio_file')
        cover_image = request.FILES.get('cover_image')
        
       
        artist, created = Artist.objects.get_or_create(
            user=request.user,
            defaults={'name': request.user.username}
        )
        
        song = Song(
            title=title,
            artist=artist, 
            audio_file=audio_file,
            cover_image=cover_image
        )
        song.save()
        
        messages.success(request, 'Bài hát đã được tạo thành công!')
        return redirect('home')
    
    return redirect('song_form')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'music_app/register.html', {'form': form})
@login_required
def profile(request):
    
    artist, created = Artist.objects.get_or_create(
        user=request.user,
        defaults={'name': request.user.username}
    )
    
    songs = Song.objects.filter(artist=artist).order_by('-created_at')
    
    return render(request, 'music_app/profile.html', {
        'artist': artist,
        'songs': songs
    })

@login_required
def update_profile(request):
   
    artist, created = Artist.objects.get_or_create(
        user=request.user,
        defaults={'name': request.user.username}
    )
    
    if request.method == 'POST':
        artist.name = request.POST.get('name')
        artist.bio = request.POST.get('bio')
        
        if 'image' in request.FILES:
            artist.image = request.FILES['image']
        
        artist.save()
        messages.success(request, 'Thông tin nghệ sĩ đã được cập nhật!')
        return redirect('profile')
    
    return render(request, 'music_app/update_profile.html', {
        'artist': artist
    })
@login_required
def update_song(request, pk):
 
    song = get_object_or_404(Song, pk=pk)
    
   
    artist = Artist.objects.get(user=request.user)
    if song.artist != artist:
        messages.error(request, 'Bạn không có quyền chỉnh sửa bài hát này!')
        return redirect('home')
    
    if request.method == 'POST':
   
        song.title = request.POST.get('title')
        
    
        if 'audio_file' in request.FILES:
            song.audio_file = request.FILES['audio_file']
       
        if 'cover_image' in request.FILES:
            song.cover_image = request.FILES['cover_image']
        
        song.save()
        messages.success(request, 'Bài hát đã được cập nhật thành công!')
        return redirect('song_detail', pk=song.pk)
    
    return render(request, 'music_app/update_song.html', {
        'song': song
    })
@login_required
def delete_song(request, pk):
   
    song = get_object_or_404(Song, pk=pk)
    
    
    artist = Artist.objects.get(user=request.user)
    if song.artist != artist:
        messages.error(request, 'Bạn không có quyền xóa bài hát này!')
        return redirect('home')
    
    if request.method == 'POST':
       
        song_title = song.title
        song.delete()
        
        messages.success(request, f'Bài hát "{song_title}" đã được xóa thành công!')
        return redirect('profile')
    
    return render(request, 'music_app/delete_song.html', {
        'song': song
    })