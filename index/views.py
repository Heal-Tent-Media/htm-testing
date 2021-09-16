from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ServicesList, TeamDetails, MailSubscriber
from .tasks import send_mail_for_subscriber
from datetime import date
from random import choice
import string
import json
from abstractaction import hashgenerator


def index(request):
    if request.method == 'GET':
        svc_list = ServicesList.objects.all().order_by('svc_id')
        team_list = TeamDetails.objects.all().order_by('tm_id')

        return render(request, 'index.html', {
            "has_header_add": "false",
            "services_list": svc_list,
            "team_list": team_list,
        })

    else:
        return render(request, '404.html', {
            "content": "Maybe the page you're looking for is not found or never existed.",
        })


def mail_subscription(request):
    if request.method == 'POST':
        response_data = {}
        subscriber_mail = str(request.POST.get('subscriber-mail'))
        subscriber_name = subscriber_mail.split("@")[0]
        # generating subscriber id
        chars = string.digits
        subscriber_id = ''.join(choice(chars) for _ in range(4))

        # calling hash generator
        verification_hash = hashgenerator.mail_verify_hash(subscriber_id, subscriber_mail)
        unsubscribe_hash = hashgenerator.unsubscribe_hash(subscriber_id, subscriber_mail)
        preference_hash = hashgenerator.preference_hash(subscriber_id, subscriber_mail)

        # generating url
        verify_url = '?id=' + str(date.today())[-2:] + '-' + subscriber_id + '&verifyuniqueurl=' + verification_hash

        if MailSubscriber.objects.filter(ms_mail=subscriber_mail).exists():
            response_data["status"] = "0"
            if MailSubscriber.objects.filter(ms_mail=subscriber_mail).filter(ms_verification_status=True):
                response_data[
                    "message"] = "It seems that your have already subscribed. We really appreciate your love 💓"
            else:
                response_data[
                    "message"] = "It seems that your have already subscribed but your mail is not yet verified"
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            subscriber = MailSubscriber()
            subscriber.ms_id = 'htm-ms-' + str(date.today())[-2:] + '-' + subscriber_id
            subscriber.ms_mail = request.POST.get('subscriber-mail')
            subscriber.ms_verification_status = False
            subscriber.ms_mail_verify_hash = verification_hash
            subscriber.ms_unsubscribe_hash = unsubscribe_hash
            subscriber.ms_preference_hash = preference_hash
            subscriber.ms_info_mail_status = True
            subscriber.ms_promotional_mail_status = True
            subscriber.ms_sub_status = True
            subscriber.ms_sub_date = date.today()
            subscriber.save()
            send_mail_for_subscriber.delay(subscriber_mail, subscriber_name, verify_url)
            response_data["status"] = "1"
            response_data[
                "message"] = "Thank you for subscribing your first pill is already on your way.\nCheck your mail 🤩"
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
    return render(request, '404.html', {
        "content": "It looks like your trying your luck or your request is invalid or never existed.",
    })


def privacy_policy(request):
    if request.method == 'GET':
        return render(request, 'privacy_policy.html', {
            "has_header_add": "false",
        })
    else:
        return render(request, '404.html', {
            "content": "It looks like your trying your luck or your request is invalid or never existed.",
        })


def cookies_policy(request):
    if request.method == 'GET':
        return render(request, 'cookies_policy.html', {
            "has_header_add": "false",
        })
    else:
        return render(request, '404.html', {
            "content": "It looks like your trying your luck or your request is invalid or never existed.",
        })


def terms_and_conditions(request):
    if request.method == 'GET':
        return render(request, 'terms_and_conditions.html', {
            "has_header_add": "false",
        })
    else:
        return render(request, '404.html', {
            "content": "It looks like your trying your luck or your request is invalid or never existed.",
        })
