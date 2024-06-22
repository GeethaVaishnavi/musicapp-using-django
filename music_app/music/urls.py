from django.urls import path
from . import views  # This should be a relative import

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
]
