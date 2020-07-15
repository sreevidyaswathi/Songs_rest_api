from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter




urlpatterns = [
    #/music/
    url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    #/music/album_id/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^Playlist/add/$',views.PlaylistCreate.as_view(),name='Playlist-add'),
]
