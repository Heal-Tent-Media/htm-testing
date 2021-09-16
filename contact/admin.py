from django.contrib import admin
from .models import Clients


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'client_name', 'org_name', 'org_web', 'client_name')
