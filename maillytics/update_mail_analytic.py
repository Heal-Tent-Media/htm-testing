from .models import MailAnalytic, CampaignDetail
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError

from .get_target_ip import get_ip


def create_target(request, cid, tid):
    geo_client = GeoIP2()
    t_ip = str(get_ip(request))

    try:
        t_country = geo_client.country(t_ip)
        t_city = geo_client.city(t_ip)
    except AddressNotFoundError:
        t_country = 'NA'
        t_city = 'NA'

    target = MailAnalytic()
    target.cid = cid
    target.tid = tid
    target.open = True
    target.clicks = 1
    target.country = t_country
    target.city = t_city
    target.save()


def update_target(request, cid, tid):
    target = MailAnalytic.objects.get(tid=tid)
    campaign = CampaignDetail.objects.get(cid=cid)
    action = request.GET.get('action')
    redirect_url = ''
    if action == 'ba':
        medium = request.GET.get('medium')
        if medium == 'li':
            redirect_url = campaign.ba[1]
            if verifyURL(redirect_url):
                target.ba[1] += 1
        elif medium == 'fb':
            redirect_url = campaign.ba[2]
            if verifyURL(redirect_url):
                target.ba[2] += 1
        elif medium == 'insta':
            redirect_url = campaign.ba[3]
            if verifyURL(redirect_url):
                target.ba[3] += 1
        elif medium == 'tw':
            redirect_url = campaign.ba[4]
            if verifyURL(redirect_url):
                target.ba[4] += 1
        elif medium == 'yt':
            redirect_url = campaign.ba[5]
            if verifyURL(redirect_url):
                target.ba[5] += 1
        else:
            redirect_url = campaign.ba[0]
            if verifyURL(redirect_url):
                target.ba[0] += 1

    elif action == 'htma':
        target.htma += 1
        redirect_url = campaign.htma

    else:
        target.ca += 1
        redirect_url = campaign.ca

    target.save()
    if redirect_url == 'null':
        redirect_url = campaign.ca

    return redirect_url


def verifyURL(url):
    if url == 'null':
        return False
    else:
        return True
