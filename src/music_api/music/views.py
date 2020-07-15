#from django.shortcuts import render
#from django.http import Http404
#from django.http import HttpResponse
#from django.template import loader
#from django.shortcuts import render
from django.views import generic
from .models import Album,Playlist
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm

from . import models




class IndexView(generic.ListView):
    template_name='music/index.html'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model=Album
    template_name='music/details.html'

class PlaylistCreate(CreateView):
    model =Playlist
    fields=['Playlist_name','song']

class UserFormView(View):

    form_class=UserForm
    template_name='music/registration_form.html'
    #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            #cleaned (normalized) data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user objects if crendtials are correct
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    #users logged in
                    login(request,user)
                    return redirect('music:index')
        return render(request,self.template_name,{'form':form})
