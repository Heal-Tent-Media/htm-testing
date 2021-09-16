from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('mail-subscription/', views.mail_subscription, name='mail-subscription'),
    path('privacy-policy/', views.privacy_policy, name="privacy-policy"),
    path('cookies-policy/', views.cookies_policy, name="cookies-policy"),
    path('terms-and-conditions/', views.terms_and_conditions, name="terms-and-conditions"),
]
