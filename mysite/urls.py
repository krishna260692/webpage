from django.urls import path
from .views import  homecontact,about,contactus,phphome,newhome




urlpatterns = [

    path('contactus', contactus, name='contactus'),
    path('homecontact', homecontact, name='homecontact'),
    path('about', about.as_view(), name='about'),
    path('phphome', phphome.as_view(), name='phphome'),
    path('newhome', newhome, name='newhome'),





]
