from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artist/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
    path('form/',views.create_form, name='song_form'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('add/', views.add_song, name='add_song'),
    path('song/<int:pk>/update/', views.update_song, name='update_song'),
    path('song/<int:pk>/delete/', views.delete_song, name='delete_song'),
    
]