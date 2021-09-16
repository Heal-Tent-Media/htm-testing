from django.http import HttpResponse
from django.shortcuts import render
from index.models import MailSubscriber
from .helper_functions import get_preference_state
from .update_subscriber_details import preference_update, unsubscribe_update


def verifyMail(request):
    if request.method == 'GET':
        subscriber_id = 'htm-ms-' + request.GET.get('id', '')
        hashurl = request.GET.get('verifyuniqueurl', '')
        if MailSubscriber.objects.filter(ms_id=subscriber_id).exists():
            if MailSubscriber.objects.filter(ms_id=subscriber_id).filter(ms_mail_verify_hash=hashurl):
                subscriber = MailSubscriber.objects.get(ms_id=subscriber_id)
                if subscriber.ms_verification_status:
                    return render(request, 'subscriber_action/verify_mail_template.html', {
                        "action_image": "already-verified",
                        "action_state": "ALREADY VERIFIED",
                        "action_response": "It seems that your email is already verified",
                        "subscribe_required": False,
                    })
                else:
                    subscriber.ms_verification_status = True
                    subscriber.save()
                    return render(request, 'subscriber_action/verify_mail_template.html', {
                        "action_image": "verified",
                        "action_state": "SUCCESS",
                        "action_response": "Your Email Verified Successfully!",
                        "subscribe_required": False,
                    })
            else:
                return render(request, 'subscriber_action/verify_mail_template.html', {
                    "action_image": "invalid",
                    "action_state": "BROKEN URL",
                    "action_response": "Typo... Check your URL that was sent to your email",
                    "subscribe_required": True,
                })
        else:
            return render(request, 'subscriber_action/verify_mail_template.html', {
                "action_image": "invalid",
                "action_state": "NOT YET SUBSCRIBED",
                "action_response": "How was that possible?",
                "subscribe_required": True,
            })
    else:
        return render(request, '404.html', {
            "content": "It looks like your trying your luck or your request is invalid or never existed.",
        })


def unsubscribe(request):
    if request.method == "GET":
        subscriber_id = 'htm-ms-' + request.GET.get('id', '')
        hashurl = request.GET.get('unsubscribeuniqueurl', '')
        if MailSubscriber.objects.filter(ms_id=subscriber_id).exists():
            if MailSubscriber.objects.filter(ms_id=subscriber_id).filter(ms_unsubscribe_hash=hashurl):
                subscriber = MailSubscriber.objects.get(ms_id=subscriber_id)
                subscriber_mail = subscriber.ms_mail
                return render(request, 'subscriber_action/unsubscribe_template.html', {
                    "mail": subscriber_mail,
                    "s_id": request.GET.get('id', ''),
                    "action_hash": str(hashurl),
                })
            return render(request, '404.html', {
                "content": "Look's like your url is broken, check your mail for a valid url to request change",
            })
        return render(request, '404.html', {
            "content": "Look's like you haven't subscribed to our mailing list yet or your url is broken",
        })
    return render(request, '404.html', {
        "content": "Your request is invalid or your trying your luck",
    })


def change_preference(request):
    if request.method == "GET":
        subscriber_id = 'htm-ms-' + str(request.GET.get('id', ''))
        hashurl = request.GET.get('preferenceuniqueurl', '')
        if MailSubscriber.objects.filter(ms_id=subscriber_id).exists():
            if MailSubscriber.objects.filter(ms_id=subscriber_id).filter(ms_preference_hash=hashurl):
                subscriber = MailSubscriber.objects.get(ms_id=subscriber_id)
                subscriber_mail = subscriber.ms_mail
                return render(request, 'subscriber_action/preference_template.html', {
                    "mail": subscriber_mail,
                    "s_id": request.GET.get('id', ''),
                    "actionhash": str(hashurl),
                    "info_status": subscriber.ms_info_mail_status,
                    "promotional_status": subscriber.ms_promotional_mail_status,
                    "current_preference_status": get_preference_state(subscriber.ms_promotional_mail_status,
                                                                      subscriber.ms_info_mail_status),
                })
            return render(request, '404.html', {
                "content": "Look's like your url is broken, check your mail for a valid url to request change",
            })
        return render(request, '404.html', {
            "content": "Look's like you haven't subscribed to our mailing list yet or your url is broken",
        })
    return render(request, '404.html', {
        "content": "Your request is invalid or your trying your luck",
    })


def action_status_unsubscribe(request):
    if request.method == "POST":
        subscriber_id = 'htm-ms-' + request.POST['s_id']
        action_hash = request.POST['action_hash']
        if MailSubscriber.objects.filter(ms_id=subscriber_id).exists():
            if MailSubscriber.objects.filter(ms_id=subscriber_id).filter(ms_unsubscribe_hash=action_hash):
                un_sub_state = request.POST['un_sub_state']
                un_sub_comment = request.POST['un_sub_cmt']
                return unsubscribe_update(subscriber_id, un_sub_state, un_sub_comment)
            return render(request, '404.html', {
                "content": "Look's like your url is broken, check your mail for a valid url to request change",
            })
        return render(request, '404.html', {
            "content": "Look's like you haven't subscribed to our mailing list yet or your url is broken",
        })

    elif request.method == "GET":
        subscriber_id = 'htm-ms-' + str(request.GET.get('id'))
        action_hash = request.GET.get('actionurl')
        print(subscriber_id, action_hash)
        if MailSubscriber.objects.filter(ms_id=subscriber_id).exists():
            if MailSubscriber.objects.filter(ms_id=subscriber_id).filter(ms_unsubscribe_hash=action_hash):
                subscriber = MailSubscriber.objects.get(ms_id=subscriber_id)
                subscriber_mail = subscriber.ms_mail
                # req_status = request.GET.get('status')
                req_update = request.GET.get('update')

                return render(request, 'subscriber_action/status_update_template.html', {
                    "title": "UNSUBSCRIPTION<br>REQUEST STATUS",
                    "action": "SUCCESSFULLY",
                    "req_update": req_update,
                    "subscriber_mail": subscriber_mail,
                })
            return render(request, '404.html', {
                "content": "Look's like your url is broken, check your mail for a valid url to request change",
            })
        return render(request, '404.html', {
            "content": "Look's like you haven't subscribed to our mailing list yet or your url is broken",
        })


def action_status_preference(request):
    if request.method == "POST":
        subscriber_id = 'htm-ms-' + request.POST['s_id']
        action_hash = request.POST['action_hash']
        if MailSubscriber.objects.filter(ms_id=subscriber_id).exists():
            if MailSubscriber.objects.filter(ms_id=subscriber_id).filter(ms_preference_hash=action_hash):
                info_state = request.POST['info_state']
                promo_state = request.POST['promo_state']
                # print("Before change >>>> ", promo_state, info_state)
                if info_state == 'true':
                    info_state = True
                else:
                    info_state = False
                if promo_state == 'true':
                    promo_state = True
                else:
                    promo_state = False
                s_details = [subscriber_id, action_hash]
                changed_state = [promo_state, info_state]
                # print("After change >>>> ", promo_state, info_state)
                current_state = request.POST['current_state']
                updated_state = get_preference_state(promo_state, info_state)
                print("c_st => ", current_state)
                print("u_st => ", updated_state)

                return preference_update(s_details, current_state, updated_state, changed_state)
            return render(request, '404.html', {
                "content": "Look's like your url is broken, check your mail for a valid url to request change",
            })
        return render(request, '404.html', {
            "content": "Look's like you haven't subscribed to our mailing list yet or your url is broken",
        })

    elif request.method == "GET":
        subscriber_id = 'htm-ms-' + str(request.GET.get('id'))
        action_hash = request.GET.get('actionurl')
        if MailSubscriber.objects.filter(ms_id=subscriber_id).exists():
            if MailSubscriber.objects.filter(ms_id=subscriber_id).filter(ms_preference_hash=action_hash):
                subscriber = MailSubscriber.objects.get(ms_id=subscriber_id)
                subscriber_mail = subscriber.ms_mail
                # req_status = request.GET.get('status')
                req_update = request.GET.get('update')

                return render(request, 'subscriber_action/status_update_template.html', {
                    "title": "CHANGE PREFERENCE<br>REQUEST STATUS",
                    "action": "SUCCESSFULLY",
                    "req_update": req_update,
                    "subscriber_mail": subscriber_mail,
                })
            return render(request, '404.html', {
                "content": "Look's like your url is broken, check your mail for a valid url to request change",
            })
        return render(request, '404.html', {
            "content": "Look's like you haven't subscribed to our mailing list yet or your url is broken",
        })
