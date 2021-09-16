from django.urls import path
from . import views

urlpatterns = [
    path('verify-mail/', views.verifyMail, name='verifyMail'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('action-status/unsubscribe/', views.action_status_unsubscribe, name='action_status_unsubscribe'),
    path('action-status/preference-update/', views.action_status_preference, name='action_status_preference'),
    path('change-preference/', views.change_preference, name='change_preference'),
]
