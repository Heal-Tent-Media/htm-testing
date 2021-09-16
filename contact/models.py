from django.db import models


class Clients(models.Model):
    client_id = models.CharField(verbose_name='client_id', primary_key=True, default='htm-cl-', max_length=15)
    client_name = models.CharField(verbose_name='client_name', default='Name', max_length=50)
    client_mail = models.CharField(verbose_name='client_mail', default='Mail', max_length=100)
    client_request = models.CharField(verbose_name='client_request', default='Service', max_length=50)
    client_quote = models.CharField(verbose_name='client_quote', default='$ 0', max_length=5)
    org_name = models.CharField(verbose_name='organization', default='Company', max_length=100)
    org_web = models.CharField(verbose_name='website', default='Company', max_length=100)
    request_time = models.CharField(verbose_name='request_time', default='', max_length=100)
