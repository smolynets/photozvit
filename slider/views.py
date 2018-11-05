from django.shortcuts import render
from .models import Photo

def index(request):
    photo = Photo.objects.all()
    return render(request, 'oksana/index.html', {'photo': photo})

def about(request):
    photo = Photo.objects.all()
    return render(request, 'oksana/about.html', {'photo': photo})
