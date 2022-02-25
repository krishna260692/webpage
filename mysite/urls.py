from django.urls import path
from .views import Home ,contact,subscribe ,reachus




urlpatterns = [

    path('home', Home.as_view(), name='home'),
    path('contact', contact, name='contact'),
    path('subscribe', subscribe, name='subscribe'),
    path('reachus', reachus, name='reachus'),



]
