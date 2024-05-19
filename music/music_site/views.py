from django.shortcuts import render
from django.http import HttpResponse
from . models import Latest,About,Playlist,Events,Blog,Gallery,Messages

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

    playlist = Playlist.objects.all()
    if len(playlist) > 0:
        playlist = Playlist.objects.order_by('pk').latest('pk')

    events = Events.objects.all()
    if len(events)>5:
        events = Events.objects.all().order_by('-pk')[:5]

    blogs = Blog.objects.all()
    if len(blogs)>5:
        blogs = Blog.objects.order_by('-pk')[:5]

    gallery = Gallery.objects.all()
    if len(gallery)>6:
        gallery = Gallery.objects.order_by('-pk')[:6]


    contxt = {"about":about,"playlist":playlist,"latest":latest,"events":events,"blogs":blogs,"gallery":gallery}

    return render(request,'music_site/index.html',contxt)

def save_messages(request):

    name = request.POST.get("name")
    contacts = request.POST.get("contacts")
    message = request.POST.get("message")
    
    resp = ""
    try:

        msg = Messages(
            name = name,
            contacts = contacts,
            message = message
        )

        msg.save()

        resp+="Message Sent Successfully, Thanks!"

    except:

        resp+="Failed to send the message"


    return HttpResponse(resp)




