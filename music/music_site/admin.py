from django.contrib import admin
from .models import Latest,About,Playlist,Album,Events,Blog

# Register your models here.

admin.site.register(Latest)
admin.site.register(About)
admin.site.register(Playlist)
admin.site.register(Album)
admin.site.register(Events)
admin.site.register(Blog)