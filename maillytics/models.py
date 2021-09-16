from django.contrib.postgres.fields import ArrayField
from django.db import models


def get_ba_defaults():
    default = 0
    action_def = (
        ('website', default),
        ('in', default),
        ('fb', default),
        ('insta', default),
        ('tw', default),
        ('yt', default),
    )

    return list(dict(action_def).values())


def get_ba_link_defaults():
    default = ''
    action_def = (
        ('website', default),
        ('in', default),
        ('fb', default),
        ('insta', default),
        ('tw', default),
        ('yt', default),
    )

    return list(dict(action_def).keys())


class MailAnalytic(models.Model):
    cid = models.CharField(verbose_name='Campaign ID', default='MPT', max_length=11)
    tid = models.CharField(verbose_name='Target ID', primary_key=True, default='', max_length=4)
    open = models.BooleanField(verbose_name='open_action', default=False, max_length=5)
    clicks = models.IntegerField(verbose_name='clicks', default=0)
    country = models.CharField(verbose_name='Country', default='', max_length=100)
    city = models.CharField(verbose_name='City', default='', max_length=100)
    ca = models.IntegerField(verbose_name='campaign_action', default=0)
    ba = ArrayField(models.IntegerField(), verbose_name='brand_action', size=6, default=get_ba_defaults)
    htma = models.IntegerField(verbose_name='htm_action', default=0)


class CampaignDetail(models.Model):
    cid = models.CharField(verbose_name='Campaign ID', primary_key=True, default='MPT', max_length=11)
    cname = models.CharField(verbose_name='Campaign Name', default='campaign', max_length=75)
    ca = models.CharField(verbose_name='campaign_action', default='', max_length=200)
    ba = ArrayField(models.CharField(max_length=100), verbose_name='brand_action', size=6, default=get_ba_link_defaults)
    htma = models.CharField(verbose_name='htm_action', default='https://healtentmedia.com', max_length=25)
