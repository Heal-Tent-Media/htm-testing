from django.db import models


class ServicesList(models.Model):
    svc_name = models.CharField(verbose_name='service_name', default="Heal Tent Service", max_length=50)
    svc_tagline = models.CharField(verbose_name='service_tagline', default="Service Tagline", max_length=100)
    svc_id = models.CharField(verbose_name='service_id', primary_key=True, blank=False, unique=True, max_length=10)
    svc_ic_url = models.CharField(verbose_name='service_ic_url', max_length=200)
    svc_des_sh = models.CharField(verbose_name='service_des_short', max_length=160, blank=False)
    svc_des_lo = models.TextField(verbose_name='service_des_long', max_length=1500)
    svc_req_url = models.CharField(verbose_name='service_request_url', max_length=200)


class TeamDetails(models.Model):
    tm_id = models.CharField(verbose_name='id', default='htm-', max_length=10)
    tm_name = models.CharField(verbose_name='name', primary_key=True, default='Name', max_length=50)
    tm_des = models.CharField(verbose_name='designation', default='Designation', max_length=50)
    tm_profile = models.URLField(verbose_name='profile_url', default='Profile URL', max_length=200)
    linkedin_id = models.CharField(verbose_name='linkedin', default='https://www.linkedin.com/in/', max_length=70)
    instagram_id = models.CharField(verbose_name='instagram', default='https://www.instagram.com/', max_length=70)
    twitter_id = models.CharField(verbose_name='twitter', default='https://twitter.com/', max_length=70)


class MailSubscriber(models.Model):
    ms_id = models.CharField(verbose_name='id', default='htm-ms-', primary_key=True, max_length=15)
    ms_mail = models.CharField(verbose_name='subscriber_mail', default='Mail', max_length=100)
    ms_verification_status = models.BooleanField(verbose_name='verification_status', default=False, max_length=5)
    ms_mail_verify_hash = models.CharField(verbose_name='mail_verification_hash', default='', max_length=175)
    ms_unsubscribe_hash = models.CharField(verbose_name='unsubscription_hash', default='', max_length=175)
    ms_preference_hash = models.CharField(verbose_name='preference_hash', default='', max_length=175)
    ms_info_mail_status = models.BooleanField(verbose_name='info_mail_status', default=False, max_length=5)
    ms_promotional_mail_status = models.BooleanField(verbose_name='promotional_mail_status', default=False, max_length=5)
    ms_update_mail_status = models.BooleanField(verbose_name='update_mail_status', default=True, max_length=5)
    ms_sub_status = models.BooleanField(verbose_name='subscription_status', default=False, max_length=5)
    ms_sub_date = models.DateField(verbose_name='subscribed_timestamp', max_length=10)
    ms_unsub_date = models.DateField(verbose_name='unsubscribed_timestamp', null=True, max_length=10)
