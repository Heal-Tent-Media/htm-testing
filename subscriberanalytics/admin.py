from django.contrib import admin
from .models import UnsubscriptionAnalytic, PreferenceAnalytic


@admin.register(UnsubscriptionAnalytic)
class UnsubscriptionAnalyticAdmin(admin.ModelAdmin):
    list_display = ('sub_id', 'uns_date', 'uns_reason')


@admin.register(PreferenceAnalytic)
class PreferenceAnalyticAdmin(admin.ModelAdmin):
    list_display = ('pref_id', 'sub_id', 'pref_date', 'pref_state')
