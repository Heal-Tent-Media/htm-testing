from django.shortcuts import render
from django.http import HttpResponse
from .models import Clients
from .tasks import send_mail_for_client
from datetime import date
from random import choice
import string


def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    else:
        return render(request, '404.html', {
            "content": "It looks like your trying your luck or your request is invalid or never existed.",
        })


def serviceRequest(request):
    if request.method == 'POST':
        # generating client id
        chars = string.digits
        client_id = ''.join(choice(chars) for _ in range(4))

        client = Clients()
        client.client_id = 'htm-cl-' + str(date.today())[-2:] + '-' + client_id
        client.client_name = request.POST.get('client-name')
        client.client_mail = request.POST.get('client-mail')
        client.org_name = request.POST.get('org-name')
        client.org_web = request.POST.get('org-web')
        client.client_request = request.POST.get('client-request')
        client.client_quote = request.POST.get('client-quote')
        client.request_time = request.POST.get('request-time')
        client.save()

        # sending mail
        print('send mail to client')
        client_details = [client.client_name, client.client_mail, client.client_request, client.request_time]
        # send_mail_for_client.delay(request.POST.get('client-mail'), request.POST.get('client-name'))
        send_mail_for_client.delay(client_details)

        return HttpResponse('Client request success')
    else:
        return render(request, '404.html', {
            "content": "It looks like your trying your luck or your request is invalid or never existed.",
        })
