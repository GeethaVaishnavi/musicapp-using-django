# urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  
    # path('', views.index, name='index'),
    path('', views.dashboard, name='dashboard'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('download/<int:song_id>/', views.download_song, name='download_song'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
