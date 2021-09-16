from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import MailAnalytic, CampaignDetail
from .update_mail_analytic import update_target, create_target


def campaignTracking(request):
    cid = request.GET.get('cid')
    tid = request.GET.get('tid')

    if 'cid' not in request.GET or 'tid' not in request.GET:
        return render(request, '404.html', {
            "content": "It looks like your trying your luck or your request is invalid or never existed.",
        })

    if CampaignDetail.objects.filter(cid=cid).exists():
        if MailAnalytic.objects.filter(tid=tid).exists():
            redirect_url = update_target(request, cid, tid)
        else:
            create_target(request, cid, tid)
            redirect_url = update_target(request, cid, tid)
        return redirect(redirect_url)
    else:
        return render(request, '404.html', {
            "content": "It looks like your trying your luck or your request is invalid or never existed.",
        })


def pixelTracking(request):

    if 'cid' not in request.GET or 'tid' not in request.GET:
        return render(request, '404.html', {
            "content": "It looks like your trying your luck or your request is invalid or never existed.",
        })

    cid = request.GET.get('cid')
    tid = request.GET.get('tid')

    if CampaignDetail.objects.filter(cid=cid).exists():
        if MailAnalytic.objects.filter(tid=tid).exists():
            target = MailAnalytic.objects.get(tid=tid)
            target.clicks += 1
            target.save()
        else:
            create_target(request, cid, tid)
        image_data = open("/home/mydev/Drop-Service/dev-htm/htm-development/static/images/maillytics/pixel-image.jpeg",
                          "rb").read()
        return HttpResponse(image_data, content_type='image/jpeg')
    else:
        return render(request, '404.html', {
            "content": "It looks like your trying your luck or your request is invalid or never existed.",
        })
