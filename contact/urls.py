from django.urls import path
from . import views

urlpatterns = [
    path('service-request/', views.serviceRequest, name='serviceRequest'),
    path('', views.contact, name='contact')
]
