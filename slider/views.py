from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Photo, Like

def index(request):
    session_key = request.session.session_key
    if not session_key:
    	request.session.cycle_key() 
    like = Like.objects.filter(session_key=session_key)
    if like:
        show = 0
    else:
        show = 1
    count = str(len(Like.objects.all()))
    photo = Photo.objects.all()
    return render(request, 'oksana/index.html', {'photo': photo, 'show': show, 'count': count})

def about(request):
    photo = Photo.objects.all()
    return render(request, 'oksana/about.html', {'photo': photo})

def like(request):
    return_dict = dict()
    session_key = request.session.session_key
    if not session_key:
    	request.session.cycle_key()
    like = Like.objects.filter(session_key=session_key)
    if not like:
        data = {}
        data['title'] = session_key
        data['session_key'] = session_key
        ts = Like(**data)
        ts.save()
    return HttpResponseRedirect(reverse('index'))
