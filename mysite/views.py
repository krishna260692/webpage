from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError ,EmailMultiAlternatives
from django.shortcuts import render
from django.conf import settings
from . import forms
from website.settings import EMAIL_HOST_USER
from django.core.mail import send_mass_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage



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
        toemail = request.POST['emailid']
        mycontact = request.POST['contact']
        message = request.POST['mycomment']

        subject="this is auto generated mail do not reply to this mail"
        from_email=settings.EMAIL_HOST_USER

        msg=f"<h1>Please find below details of {name}</h1>" \
            f"<h1><b> Name </b>: { name} </h1>" \
            f"<h1><b>Email_id</b>: { toemail} </h1>" \
            f"<h1><b>Contact_No</b>: { mycontact} </h1>" \
            f"<h1><b>Message</b>: { message} </h1>"

        to='krishna260692@gmail.com'
        msg = EmailMultiAlternatives(subject, msg, from_email, [to])
        msg.content_subtype='html'
        msg.send()

        send_mail(
            "autogenerated mail do not reply",
            'your message has been successfully sent, we will contact you soon',
            from_email,
            [toemail],
            fail_silently=False,
        )










    return render(request, 'contacttwo.html')










