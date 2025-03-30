from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artist/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
]