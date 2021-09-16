from django.urls import path
from . import views

urlpatterns = [
    path('get-analytics/', views.get_analytics, name='get_analytics'),
]
