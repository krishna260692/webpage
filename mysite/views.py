from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from . import forms
from website.settings import EMAIL_HOST_USER


class Home(TemplateView):
    template_name = "mysite/home1.html"

def contact(request):
    if request.method == 'POST':
        entername = request.POST['entername']
        entermail = request.POST['entermail']

        send_mail('Hello','Thank you for visting our website, we will contact you soon!',
            settings.EMAIL_HOST_USER,
            [entermail],
            fail_silently=False,)
        return render(request, 'success.html')
    return render(request, 'contactus.html')

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(
            subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form':sub})




def reachus(request):
    if request.method == 'POST':
        name = request.POST['fname']
        lastname = request.POST['lname']
        mycontact = request.POST['contact']
        massage = request.POST['mycomment']

        print(name,lastname,mycontact,massage)






    return render(request, 'contacttwo.html')










