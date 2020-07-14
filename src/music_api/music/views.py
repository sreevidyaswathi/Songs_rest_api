from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Album

# Create your views here.
def index(request):
    all_albums=Album.objects.all()
    template=loader.get_template('music/index.html')
    #html=''
    #for album in all_albums:
    #    url='/music/' +str(album.id) +'/'
    #    html+='<a href="'+url+'">' +album.album_title+'</a><br>'
    return HttpResponse('')

def detail(request,album_id):
    return HttpResponse("<h2>Details of Album id: " +str(album_id)+"</h2>")
