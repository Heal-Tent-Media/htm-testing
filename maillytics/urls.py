from django.urls import path
from . import views

urlpatterns = [
    path('image/', views.pixelTracking, name="pixelTracking"),
    path('', views.campaignTracking, name="campaignTracking"),
]
