from django.shortcuts import render
from . models import Latest,About,Playlist,Events,Blog

# Create your views here.


'''
    index page route
'''
def index(request):
    latest = Latest.objects.all()
    if len(latest)>0:
        latest = Latest.objects.order_by('pk').latest('pk')
    
    about = About.objects.all()
    if len(about)>0:
        about = About.objects.order_by('pk').latest('pk')

    events = Events.objects.all()
    if len(events)>5:
        events = Events.objects.all().order_by('-pk')[:5]

    blogs = Blog.objects.all()
    if len(blogs)>5:
        blogs = Blog.objects.order_by('-pk')[:5]


    contxt = {"about":about,"latest":latest,"events":events,"blogs":blogs}

    return render(request,'music_site/index.html',contxt)
