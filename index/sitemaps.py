from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from datetime import datetime


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'
    protocol = 'https'
    date_format = '%Y-%m-%d %H:%M:%S'
    date_now = '2021-07-02 08:00:00'
    lastmod = datetime.strptime(date_now, date_format)

    def items(self):
        return ['index', 'contact']

    def location(self, item):
        return reverse(item)
