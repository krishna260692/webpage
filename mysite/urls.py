from django.urls import path
from .views import  homecontact,about,form ,contactus




urlpatterns = [


    path('homecontact', homecontact, name='homecontact'),
    path('about', about.as_view(), name='about'),
    path('contactus', contactus.as_view(), name='contactus'),
    path('form', form , name='form'),






]
