from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def index(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        content = request.POST['content']
        send_to = request.POST['send_to']
        number = int(request.POST['number'])

        for i in range(number):
            send_mail(subject,content,settings.EMAIL_HOST_USER,send_to.split(','))
        
        return HttpResponse('messgae sent')

    else:    
        return render(request,'index.html')
    
