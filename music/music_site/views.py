from django.shortcuts import render
from . models import Latest,About,Playlist

# Create your views here.


'''
    index page route
'''
def index(request):
    latest = Latest.objects.all()
    if len(latest)>0:
        latest = Latest.objects.order_by('pk').latest('pk')
    
        
    about = About.objects.order_by('pk').latest('pk')


    contxt = {"about":about,"latest":latest}

    return render(request,'music_site/index.html',contxt)
