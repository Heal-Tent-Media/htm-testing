"""healtentmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from index.sitemaps import StaticViewSitemap

sitemaps = {
    'staticSitemap': StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-analytics/', include('subscriberanalytics.urls')),
    path('', include('index.urls')),
    path('contact/', include('contact.urls')),
        path('maillytics/', include('maillytics.urls')),
    path('subscriber-action/', include('subscriberaction.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
