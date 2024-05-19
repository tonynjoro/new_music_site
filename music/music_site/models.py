from django.db import models
#from rembg import remove
from PIL import Image

# Create your models here.

class Latest(models.Model):

    description = models.TextField()
    link= models.TextField(default="",verbose_name="Paste Embed code of latest Video")

    class Meta:

        verbose_name = "Latest Video"
        verbose_name_plural = "Latest Video"
'''
This details to be posted on about section
'''
class About(models.Model):

    about = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='about_images')

    # remove image background
    '''
    def save(self):
        super().save() 

        img = Image.open(self.image.path)
        new_img = remove(img)
        new_img.save(self.image.path)

    '''
    class Meta:

        verbose_name = "About"
        verbose_name_plural = "About"

        

class Playlist(models.Model):

    title  = models.CharField(max_length=100)
    playlist = models.CharField(max_length=1000, verbose_name="paste embed code for youtube playlist" ,default="")

    def __str__(self):

        return str(self.title)
    
    class Meta:

        verbose_name = "Playlist"
        verbose_name_plural = "Playlist"
    
class Album(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField()
    link = models.CharField(max_length=1000, verbose_name = "paste embed code for youtube album", default="")

    def __str__(self):

        return str(self.title)
    
    def save(self):
        super().save() 

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 800:
            new_img = (300, 800)
            img.thumbnail(new_img)
            img.save(self.image.path)
    class Meta:

        verbose_name = "Album"
        verbose_name_plural = "Albums"
    
class Events(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    pin_location = models.TextField(null=True)
    date = models.DateField()
    image = models.ImageField(upload_to='events_images')

    def save(self):
        super().save() 

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 800:
            new_img = (300, 800)
            img.thumbnail(new_img)
            img.save(self.image.path)
    class Meta:

        verbose_name = "Events"
        verbose_name_plural = "Events"


class Blog(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='events_images')

    def save(self):
        super().save() 

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 800:
            new_img = (300, 800)
            img.thumbnail(new_img)
            img.save(self.image.path)

    class Meta:

        verbose_name = "Blog & News"
        verbose_name_plural = "Blog & News"


class Gallery(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery_images")

    def __str__(self):

        return str(self.title)
    
    class Meta:

        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"


class Messages(models.Model):

    name = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):

        return "Name:  "+str(self.name)+" || Contacts:  "+self.contacts
    
    class Meta:

        verbose_name = "Messages"
        verbose_name_plural = "Messages"








    


