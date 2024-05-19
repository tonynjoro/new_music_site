from django.urls import path 
from . import views 
from .views import index,save_messages

urlpatterns = [

    path('',views.index,name="site-index"),
    path('save_messages',views.save_messages,name="site-save-messages")
]