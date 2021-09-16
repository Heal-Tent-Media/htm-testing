from django.contrib import admin
from .models import ServicesList, TeamDetails, MailSubscriber


@admin.register(ServicesList)
class ServiceListAdmin(admin.ModelAdmin):
    list_display = ('svc_id', 'svc_name', 'svc_tagline', 'svc_ic_url')


@admin.register(TeamDetails)
class TeamDetailsAdmin(admin.ModelAdmin):
    list_display = ('tm_name', 'tm_des', 'tm_profile')


@admin.register(MailSubscriber)
class MailSubscriberAdmin(admin.ModelAdmin):
    list_display = ('ms_id', 'ms_sub_status', 'ms_sub_date', 'ms_verification_status')
