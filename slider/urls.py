from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from sliderdb.settings import DEBUG

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-author', views.about, name='about'),
    path('like', views.like, name='like'),
] 

if DEBUG == True:
    from django.conf.urls.static import static
    from django.conf import settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
