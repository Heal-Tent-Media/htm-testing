from django.db import models
from django.utils.timezone import now


class UnsubscriptionAnalytic(models.Model):
    sub_id = models.CharField(verbose_name='subscriber_id', default='htm-ms-', primary_key=True, max_length=15)
    uns_reason = models.CharField(verbose_name='unsubscription_reason', default='unsr-000', max_length=8)
    uns_comment = models.CharField(verbose_name='comments', default='', max_length=150)
    uns_date = models.DateField(verbose_name='unsubscribed_timestamp', null=False, max_length=10)


class PreferenceAnalytic(models.Model):
    pref_id = models.CharField(verbose_name='preference_id', default='', primary_key=True, max_length=5)
    sub_id = models.CharField(verbose_name='subscriber_id', default='htm-ms-', max_length=15)
    pref_state = models.CharField(verbose_name='preference_state', default='', max_length=8)
    pref_date = models.DateField(verbose_name='changed_timestamp', null=False, max_length=10)


class AdminAccessAnalytic(models.Model):
    admin_name = models.CharField(verbose_name='name', default='htm-', max_length=30)
    admin_id = models.CharField(verbose_name='admin_id', default='htm-ana-admin-', primary_key=True, max_length=20)
    access_hash = models.CharField(verbose_name='access_hash', default='', max_length=175)
    last_req = models.TimeField(verbose_name='last_request', default=now, editable=False)
    total_req = models.CharField(verbose_name='total_requests', default='', max_length=5)
    req_type = models.CharField(verbose_name='request_type', default='', max_length=25)
