from django.shortcuts import render
from .models import Photo

def index(request):
    photo = Photo.objects.all()
    return render(request, 'oksana/index.html', {'photo': photo})
