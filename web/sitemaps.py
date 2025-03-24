from django.contrib.sitemaps import Sitemap
from .models import Product, News
from django.urls import reverse

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    i18n = True

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.created_at

class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    i18n = True

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.created_at
    
class IndexSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0
    i18n = True

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)
    
class ContactSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6
    i18n = True

    def items(self):
        return ['contact']

    def location(self, item):
        return reverse(item)