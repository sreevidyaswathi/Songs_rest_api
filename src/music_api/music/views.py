from django.shortcuts import render
from django.http import Http404
#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import Album

# Create your views here.
def index(request):
    all_albums=Album.objects.all()
    #template=loader.get_template('music/index.html'
    #html=''
    #for album in all_albums:
    #    url='/music/' +str(album.id) +'/'
    #    html+='<a href="'+url+'">' +album.album_title+'</a><br>'
    #return HttpResponse(template.render(context,request))
    return render(request,'music/index.html',{'all_albums':all_albums,})

def detail(request,album_id):
    try:
          album= Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
          raise Http404("Album Does Not exist")
    return render(request,'music/details.html',{'album':   album })
    #return HttpResponse("<h2>Details of Album id: " +str(album_id)+"</h2>")
