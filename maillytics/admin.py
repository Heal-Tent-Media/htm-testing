from django.contrib import admin
from .models import MailAnalytic, CampaignDetail


@admin.register(MailAnalytic)
class MailAnalyticAdmin(admin.ModelAdmin):
    list_display = ('cid', 'tid', 'open', 'clicks', 'country', 'city')


@admin.register(CampaignDetail)
class CampaignListAdmin(admin.ModelAdmin):
    list_display = ('cid', 'cname')
